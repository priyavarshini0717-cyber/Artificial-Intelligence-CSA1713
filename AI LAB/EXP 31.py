from sklearn.neighbors import KNeighborsClassifier
X = [
    [1, 2],
    [2, 3],
    [3, 3],
    [6, 7],
    [7, 8],
    [8, 8]
]
Y = ['A', 'A', 'A', 'B', 'B', 'B']
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, Y)
new_data = [[4, 4]]
prediction = knn.predict(new_data)
print("K-NEAREST NEIGHBORS CLASSIFICATION")
print("----------------------------------")

print("Training Data:", X)
print("Class Labels:", Y)
print("K Value:", 3)

print("\nNew Data:", new_data)
print("Predicted Class:", prediction[0])
