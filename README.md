# 🎬 Movie Recommendation System

A simple and intuitive Movie Recommendation System built using Python, Pandas, Scikit-learn, and Streamlit. It allows users to select a movie and get five similar movie recommendations, complete with poster images fetched from the OMDB API.

![image](https://github.com/user-attachments/assets/03d8705c-257b-4049-a312-7c3baee9786c)

# 🚀 Features

Recommends 5 similar movies based on content similarity.
Displays movie posters using the OMDB API.
Clean and interactive web UI powered by Streamlit.
Utilizes precomputed similarity matrix for fast results.

# 🧠 How It Works

A movie is selected by the user.
A similarity score (cosine similarity) is calculated from a precomputed matrix.
The top 5 most similar movies are retrieved.
Poster images are fetched in real time from the OMDB API using movie titles.
Recommendations are displayed side-by-side with posters and titles.

## 🗂 Project Structure

movie_recommendation_system/

│

├── app.py                 # Main Streamlit app

├── movies_dict.pkl        # Movie metadata dictionary (title, etc.)

├── similarity.pkl         # Precomputed similarity matrix

├── README.md              # This file

├── requirements.txt       # Python dependencies

└── .venv/                 # Virtual environment (optional, not uploaded)

## 🔧 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/anamipatel81/Movie-recommendation-system.git
   cd Movie-recommendation-system
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

## Run the Streamlit app:
    ```bash
    streamlit run app.py

**📌 Future Improvements**

Add genre-based or collaborative filtering.

Use IMDb IDs for more accurate poster matching.

Add user login and personalized history.
