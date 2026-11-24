from sklearn.svm import SVC
X = [
    [1, 40],
    [2, 45],
    [3, 50],
    [6, 80],
    [7, 85],
    [8, 90]
]
Y = [0, 0, 0, 1, 1, 1]

model = SVC(kernel='linear')

model.fit(X, Y)

new_data = [[5, 70]]
prediction = model.predict(new_data)

print("SUPPORT VECTOR MACHINE")
print("----------------------")

print("Training Data:", X)
print("Class Labels:", Y)

print("\nNew Data:", new_data)

if prediction[0] == 1:
    print("Predicted Class: PASS")
else:
    print("Predicted Class: FAIL")
