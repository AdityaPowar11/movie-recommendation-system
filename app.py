import streamlit as st
import pickle
import requests

# Load data
movies_list = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

# Movie titles
movies = movies_list['title'].values


def fetch_posters(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"

    params = {
        "api_key": "8265bd1679663a7ea12ac168da84d2e8",
        "language": "en-US"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None

    data = response.json()

    if data.get("poster_path"):
        return "https://image.tmdb.org/t/p/w500" + data["poster_path"]

    return None


def recommend(movie):

    movie_index = movies_list[
        movies_list['title'] == movie
    ].index[0]

    distances = similarity[movie_index]

    # Get top 5 similar movies
    movie_indices = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movie_indices:

        movie_title = movies_list.iloc[i[0]]['title']
        movie_id = movies_list.iloc[i[0]]['movie_id']

        recommended_movies.append(movie_title)
        recommended_posters.append(fetch_posters(movie_id))

    return recommended_movies, recommended_posters


# -----------------------------
# Streamlit UI
# -----------------------------

st.title("🎬 Movie Recommendation System")

selected_movie = st.selectbox(
    "Select a movie",
    movies
)

if st.button("Recommend"):

    names, posters = recommend(selected_movie)

    st.subheader("Recommended Movies")

    cols = st.columns(5)

    for i in range(5):

        with cols[i]:

            st.text(names[i])

            if posters[i]:
                st.image(posters[i], use_container_width=True)
            else:
                st.write("Poster not available")