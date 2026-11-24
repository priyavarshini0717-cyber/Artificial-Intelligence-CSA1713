import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
ratings = np.array([
    [5, 4, 0, 0, 1],
    [4, 5, 0, 0, 2],
    [0, 0, 5, 4, 5],
    [0, 0, 4, 5, 4],
    [5, 4, 0, 0, 0]
])

similarity = cosine_similarity(ratings)

user_id = 4

user_ratings = ratings[user_id]
similar_users = similarity[user_id]

predicted_scores = np.dot(similar_users, ratings) / np.sum(similar_users)

recommendations = []

for movie in range(len(user_ratings)):
    if user_ratings[movie] == 0:
        recommendations.append(
            (movie, predicted_scores[movie])
        )
recommendations.sort(key=lambda x: x[1], reverse=True)

print("COLLABORATIVE FILTERING")
print("-----------------------")

print("Target User: User", user_id + 1)

print("\nRecommended Movies:")

for movie, score in recommendations:
    print("Movie", movie + 1,
          "- Predicted Rating:", round(score, 2))

