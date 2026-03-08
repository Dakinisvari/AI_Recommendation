# AI-Enabled Recommendation Engine for an E-Commerce Platform

This project implements an **AI-powered product recommendation system** for an e-commerce platform.
The system analyzes user behavior and product information to recommend relevant products to users.

The project demonstrates two recommendation techniques:

* **Content-Based Filtering**
* **Collaborative Filtering**

These techniques help improve **user experience, product discovery, and sales conversion** in e-commerce platforms.

---

# 📂 Project Structure

```
AI recommendation/
│
├── cleaned_data.csv
├── cleaning_data.py
├── collaborative_filtering.py
├── content_based.py
├── preprocess_data.py
├── requirements.txt
└── README.md
```

---

# 📌 Phase 1: Data Cleaning and Preprocessing

Raw datasets often contain:

* Missing values
* Invalid IDs
* Inconsistent formats

These issues must be handled before building recommendation models.

### Data Cleaning Tasks Performed

* Replaced invalid or inconsistent values with `NaN`
* Converted ID columns to numeric format
* Removed rows containing missing or null values
* Cleaned `ProdID` column by dropping invalid entries
* Ensured overall data consistency and integrity
* Reset dataset index after cleaning

The cleaned dataset is saved as:

```
cleaned_data.csv
```

---

# 🤖 Phase 2: Content-Based Recommendation System

The **content-based recommender** suggests products similar to a selected product based on product features.

### Method Used

* TF-IDF (Term Frequency – Inverse Document Frequency)
* Cosine Similarity

### Workflow

1. Convert product **tags into TF-IDF vectors**
2. Calculate **cosine similarity between products**
3. Identify **products most similar to the selected product**
4. Recommend the **top N similar products**

### Example Output

```
Recommended Products for:
OPI Infinite Shine Nail Polish

1. Essie Gel Couture Nail Polish
2. Sally Hansen Miracle Gel Nail Color
3. Revlon Nail Enamel
```

---

# 👥 Phase 3: Collaborative Filtering Recommendation System

Collaborative filtering recommends products based on **similar user behavior**.

### Method Used

* User–Item Matrix
* Cosine Similarity

### Workflow

1. Create a **User–Item Matrix**
2. Compute **similarity between users**
3. Identify **users with similar rating patterns**
4. Recommend products that **similar users liked but the target user has not rated**

### Example Output

```
Top 5 Recommendations for User 4

1. Wahl Color Pro Plus Haircut Kit
2. Oral-B Disney Star Wars Kids Toothbrush
3. Dr. Hauschka Revitalizing Day Cream
4. Clairol Nice N Easy Hair Color
5. DevLon Paraffin Wax Refill Spa
```

---

# 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Git
* GitHub

---

# ⚙️ Installation

Clone the repository:

```
git clone https://github.com/yourusername/recommendation-engine.git
```

Navigate to the project directory:

```
cd recommendation-engine
```

Install required libraries:

```
pip install -r requirements.txt
```

---

# ▶️ How to Run

Run data cleaning:

```
python cleaning_data.py
```

Run content-based recommendation:

```
python content_based.py
```

Run collaborative filtering:

```
python collaborative_filtering.py
```

# 👩‍💻 Author

**Dakinisvari S**
