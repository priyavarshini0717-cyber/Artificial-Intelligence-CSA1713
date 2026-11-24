from sklearn.tree import DecisionTreeClassifier
X = [
    [22, 20000],
    [25, 25000],
    [28, 30000],
    [35, 50000],
    [40, 60000],
    [45, 70000]
]
Y = [0, 0, 0, 1, 1, 1]
model = DecisionTreeClassifier(random_state=0)
model.fit(X, Y)
new_data = [[38, 55000]]
prediction = model.predict(new_data)
print("DECISION TREE CLASSIFICATION")
print("----------------------------")

print("Training Data:", X)
print("Class Labels:", Y)

print("\nNew Data:", new_data)
if prediction[0] == 1:
    print("Predicted Class: Eligible")
else:
    print("Predicted Class: Not Eligible")
