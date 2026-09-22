# 🎬 Movie Recommendation System

A simple **content-based movie recommendation system** built with Python and Streamlit. Select a movie and get 5 similar movie recommendations along with their posters.

## 🌐 Live Demo

👉 **[Try the Movie Recommendation System](https://cinemar.streamlit.app/)**

## 🚀 Features

* 🎥 Select a movie from the dropdown
* 🤖 Get 5 similar movie recommendations
* 🖼️ Display movie posters using the TMDB API
* ⚡ Interactive Streamlit interface
* 📊 Content-based movie similarity

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* Requests
* TMDB API
* Pickle

## ⚙️ How It Works

1. Movie data is processed and converted into useful features.
2. Similarity between movies is calculated.
3. The similarity data is stored using Pickle.
4. The user selects a movie.
5. The system finds the 5 most similar movies.
6. Movie posters are retrieved using the TMDB API.
7. The recommendations are displayed in the Streamlit application.

## 📂 Project Structure

```text
movie-recommendation-system/
│
├── app.py
├── movies.pkl
├── similarity.pkl
├── movie-recommender-system.ipynb
├── requirements.txt
├── .gitignore
└── README.md
```

## 💻 Run Locally

Clone the repository:

```bash
git clone https://github.com/AdityaPowar11/movie-recommendation-system.git
```

Open the project:

```bash
cd movie-recommendation-system
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## 🔑 TMDB API

The application uses the **TMDB API** to retrieve movie posters.

Store your API key securely using Streamlit secrets rather than directly exposing it in `app.py`.

Example:

```toml
TMDB_API_KEY = "your_api_key"
```

## 🎯 Future Improvements

* Add movie ratings
* Add genres and release dates
* Add movie descriptions
* Improve UI/UX
* Add personalized recommendations
* Deploy additional recommendation models

## 👨‍💻 Author

**Aditya Powar**

GitHub: [AdityaPowar11](https://github.com/AdityaPowar11)

## 🌐 Live Application

**[cinemar.streamlit.app](https://cinemar.streamlit.app/)**
