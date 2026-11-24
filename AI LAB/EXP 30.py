from sklearn.linear_model import LinearRegression
X = [[1], [2], [3], [4], [5]]
Y = [20, 30, 40, 50, 60]
model = LinearRegression()
model.fit(X, Y)
hours = [[6]]
prediction = model.predict(hours)
print("LINEAR REGRESSION")
print("--------------------------")

print("Training Data:")
print("Hours Studied:", X)
print("Marks Obtained:", Y)

print("\nPrediction Result:")
print("Hours Studied:", hours[0][0])
print("Predicted Marks:", round(prediction[0], 2))

print("\nModel Performance:")
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
print("R2 Score:", model.score(X, Y))
