from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


def collaborative_filtering_recommendations(data, target_user_id, top_n=10):

    # STEP 1: CREATE USER-ITEM MATRIX
    user_item_matrix = data.pivot_table(
        index="User's ID",
        columns="ProdID",
        values="Rating",
        aggfunc="mean"
    ).fillna(0)

    # STEP 2: CHECK IF USER EXISTS
    if target_user_id not in user_item_matrix.index:
        print("User not found.")
        return pd.DataFrame()

    # STEP 3: CALCULATE USER SIMILARITY
    user_similarity = cosine_similarity(user_item_matrix)

    # STEP 4: FIND TARGET USER INDEX
    target_user_index = user_item_matrix.index.get_loc(target_user_id)

    # STEP 5: GET SIMILARITY SCORES
    user_similarities = user_similarity[target_user_index]

    # STEP 6: SORT SIMILAR USERS
    similar_users_indices = user_similarities.argsort()[::-1][1:]

    recommended_items = []

    # STEP 7: FIND PRODUCTS RATED BY SIMILAR USERS
    for user_index in similar_users_indices:

        similar_user_ratings = user_item_matrix.iloc[user_index]
        target_user_ratings = user_item_matrix.iloc[target_user_index]

        # similar user rated & target user not rated
        candidate_items = (similar_user_ratings > 0) & (target_user_ratings == 0)

        items = user_item_matrix.columns[candidate_items]

        recommended_items.extend(items)

    # STEP 8: REMOVE DUPLICATES
    recommended_items = list(dict.fromkeys(recommended_items))

    # STEP 9: LIMIT TO TOP N
    recommended_items = recommended_items[:top_n]

    # STEP 10: RETURN PRODUCT DETAILS
    recommended_items_details = data[data['ProdID'].isin(recommended_items)][['ProdID','Name','Review Count','Brand','ImageURL','Rating']].drop_duplicates(subset='ProdID').head(top_n)
    return recommended_items_details


# Example usage
target_user_id = 4
top_n = 5
data = pd.read_csv(r"D:\AI recommendation\cleaned_data.csv")
collaborative_filtering_rec = collaborative_filtering_recommendations(data, target_user_id, top_n)

print(f"Top {top_n} recommendations for user {target_user_id}:\n")
print(collaborative_filtering_rec)