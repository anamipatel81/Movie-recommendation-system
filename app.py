import streamlit as st
import pickle
import pandas as pd
import requests

# Function to fetch poster using OMDB API with movie title
def fetch_poster_by_title(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey=a7612589"
    response = requests.get(url)
    data = response.json()
    if data.get('Response') == 'True':
        return data['Poster']
    else:
        print(f"OMDB Error: {data.get('Error')} for title: {title}")
        return "https://via.placeholder.com/150"  # default image

# Recommend function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movie_list:
        title = movies.iloc[i[0]].title
        poster = fetch_poster_by_title(title)
        recommended_movies.append(title)
        recommended_posters.append(poster)

    return recommended_movies, recommended_posters

# Streamlit UI
st.title('Movie Recommendation System')

# Load data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

selected_movie_name = st.selectbox(
    "Select a movie to get recommendations:",
    movies['title'].values
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    # Show recommendations in a row
    cols = st.columns(5)
    for idx in range(5):
        with cols[idx]:
            st.text(names[idx])
            st.image(posters[idx])
