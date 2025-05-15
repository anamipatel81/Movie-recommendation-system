**🎬 Movie Recommendation System**

A simple and intuitive Movie Recommendation System built using Python, Pandas, Scikit-learn, and Streamlit. It allows users to select a movie and get five similar movie recommendations, complete with poster images fetched from the OMDB API.

**🚀 Features**

Recommends 5 similar movies based on content similarity.

Displays movie posters using the OMDB API.

Clean and interactive web UI powered by Streamlit.

Utilizes precomputed similarity matrix for fast results.

**🧠 How It Works**

A movie is selected by the user.

A similarity score (cosine similarity) is calculated from a precomputed matrix.

The top 5 most similar movies are retrieved.

Poster images are fetched in real time from the OMDB API using movie titles.

Recommendations are displayed side-by-side with posters and titles.

**🗂 Project Structure**

movie_recommendation_system/

│

├── app.py                 # Main Streamlit app

├── movies_dict.pkl        # Movie metadata dictionary (title, etc.)

├── similarity.pkl         # Precomputed similarity matrix

├── README.md              # This file

├── requirements.txt       # Python dependencies

└── .venv/                 # Virtual environment (optional, not uploaded)

**🔧 Installation**

Clone the repository:

git clone https://github.com/yourusername/movie_recommendation_system.git
cd movie_recommendation_system


Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run app.py


**🔑 API Key**

This project uses the OMDB API to fetch poster images.

You need an API key (already included in app.py):

http://www.omdbapi.com/?t=MovieTitle&apikey=a7612589

You can get your own key if needed.

**✅ Requirements**

Python 3.7+

Streamlit

Pandas

Scikit-learn

Requests

Pickle (standard lib)


**📌 Future Improvements**

Add genre-based or collaborative filtering.

Use IMDb IDs for more accurate poster matching.

Add user login and personalized history.

**💡 Credits**

Movie data: Your dataset (preprocessed into movies_dict.pkl)

Poster images: OMDB API

UI: Streamlit

**📜 License**

This project is open-source and available under the MIT License.
