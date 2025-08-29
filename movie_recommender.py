import pandas as pd

# Step 1: Load datasets
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

# Step 2A: Compute average rating & number of ratings per movie
agg = ratings.groupby('movieId').rating.agg(['mean', 'count']).reset_index()
agg.columns = ['movieId', 'avg_rating', 'num_ratings']

# Step 2B: Merge with movies table
df = movies.merge(agg, on='movieId', how='left')

# Step 2C: Fill missing values
df['avg_rating'] = df['avg_rating'].fillna(0)
df['num_ratings'] = df['num_ratings'].fillna(0).astype(int)

# Step 3: Weighted Rating (formula: avg_rating * num_ratings)
df['weighted_rating'] = df['avg_rating'] * df['num_ratings']
print(df.head(10).to_string(index=False))

# Step 4: Recommendation Logic
print("\n Top 10 Movies Overall:")
top_movies = df.sort_values(by="weighted_rating", ascending=False).head(10)
print(top_movies[['title', 'genres', 'avg_rating', 'num_ratings', 'weighted_rating']].to_string(index=False))

print("\n Most Popular 5 Movies (by rating count):")
popular_movies = df.sort_values(by="num_ratings", ascending=False).head(5)
print(popular_movies[['title', 'genres', 'avg_rating', 'num_ratings']].to_string(index=False))

# Step 4B: Recommend movies for a specific user
user_id = int(input("Enter User ID: "))

# Movies already watched
watched = ratings[ratings['userId'] == user_id].merge(movies, on='movieId')
print("\n Movies already watched by User", user_id)
print(watched[['title', 'rating']])

# Favorite genre of this user
genre_ratings = (
    watched.groupby('genres').rating.mean().reset_index()
    .sort_values('rating', ascending=False)
)
fav_genre = genre_ratings.iloc[0]['genres']
print("\n Favorite Genre of User", user_id, ":", fav_genre)

# Movies not watched yet
unwatched = df[~df['movieId'].isin(watched['movieId'])]

# Recommend top 5 in favorite genre
recommendations = (
    unwatched[unwatched['genres'].str.contains(fav_genre, case=False, na=False)]
    .sort_values('weighted_rating', ascending=False)
    .head(5)
)

if recommendations.empty:
    print("\n No recommendations available for this user in their favorite genre.")
else:
    print("\n Recommended Movies for User", user_id, "(", fav_genre, "):")
    print(
        recommendations[['title', 'genres', 'avg_rating', 'num_ratings', 'weighted_rating']]
        .to_string(index=False)
    )
