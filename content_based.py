from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


def content_based_recommendation(data, item_name, top_n=10):

    # STEP 1: CHECK IF PRODUCT EXISTS
    if item_name not in data['Name'].values:
        print("Item not found in the dataset.")
        return pd.DataFrame()

    # STEP 2: CONVERT TEXT (TAGS) INTO NUMBERS USING TF-IDF
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(data['Tags'])

    # STEP 3: CALCULATE COSINE SIMILARITY
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # STEP 4: FIND PRODUCT INDEX
    item_index = data[data['Name'] == item_name].index[0]

    # STEP 5: GET SIMILARITY SCORES
    similarity_scores = list(enumerate(cosine_sim[item_index]))

    # STEP 6: SORT BY SIMILARITY
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # STEP 7: REMOVE THE PRODUCT ITSELF
    similarity_scores = similarity_scores[1:top_n+1]

    # GET INDICES OF SIMILAR PRODUCTS
    product_indices = [i[0] for i in similarity_scores]

    # STEP 8: FETCH PRODUCT DETAILS
    recommended_products = data.iloc[product_indices][['Name', 'Brand']]

    return recommended_products


# LOAD DATASET
data = pd.read_csv(r"D:\AI recommendation\cleaned_data.csv")

# CLEAN TAGS COLUMN
data['Tags'] = data['Tags'].fillna('')

# PRODUCT TO SEARCH
item_name = "OPI Infinite Shine, Nail Lacquer Nail Polish, Bubble Bath"

# GET RECOMMENDATIONS
recommendations = content_based_recommendation(data, item_name, top_n=8)

print(recommendations)