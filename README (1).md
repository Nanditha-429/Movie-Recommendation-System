# 🎬 Movie Recommendation System (Pandas Project)

## 📌 Overview
This is a simple **Movie Recommendation System** built using **Python (Pandas)**.  
It analyzes movie ratings and recommends movies based on:
- **Weighted ratings** (average rating × number of ratings)
- **Most popular movies**
- **Personalized recommendations** based on a user’s favorite genre.

This project was created as part of learning **Pandas** and practicing data analysis.

---

## 🛠️ Tech Stack
- Python 🐍
- Pandas
- CSV datasets (`movies.csv`, `ratings.csv`)

---

## 📂 Dataset
The project uses two CSV files:
1. **movies.csv** → Contains movie titles & genres  
2. **ratings.csv** → Contains user ratings for movies  

---

## 🚀 Features
✔️ Load and clean movie & ratings data  
✔️ Compute **average rating** and **number of ratings** per movie  
✔️ Calculate **weighted ratings**  
✔️ Show **Top 10 movies overall**  
✔️ Show **Most popular 5 movies**  
✔️ Recommend **Top 5 movies** for a specific user based on their **favorite genre**  

---

## ▶️ How to Run
1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/movie-recommendation-system.git
   ```
2. Navigate into the folder:
   ```bash
   cd movie-recommendation-system
   ```
3. Run the script:
   ```bash
   python movie_recommender.py
   ```

---

## 📊 Example Output
```
Top 10 Movies Overall:
title          | genres        | avg_rating | num_ratings | weighted_rating
The Matrix     | Action|Sci-Fi | 4.5        | 500         | 2250
...

Most Popular 5 Movies:
title          | genres        | avg_rating | num_ratings
Titanic        | Drama|Romance | 4.2        | 600
...

Recommended Movies for User 1 (Action):
title          | genres        | avg_rating | num_ratings | weighted_rating
Die Hard       | Action        | 4.3        | 450         | 1935
...
```

---

## 📌 Future Improvements
- Add collaborative filtering (user-based recommendations)  
- Use cosine similarity for better recommendations  
- Build a web UI using **Streamlit**  

---

## ✨ Author
👩‍💻 Nanditha  
Student at Sreyas Institute of Engineering and Technology  
