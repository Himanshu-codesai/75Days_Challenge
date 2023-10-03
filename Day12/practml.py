# Example input data
from sklearn.linear_model import LogisticRegression
X = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
y = [0, 0, 1, 1, 1]

# Train a model
model = LogisticRegression()
model.fit(X, y)

# Make a prediction
prediction = model.predict([[1, 3]])
print(prediction)
# print(X)