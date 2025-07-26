from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import pickle
import os

iris = load_iris()
X, y = iris.data, iris.target
model = LogisticRegression(max_iter=200)
model.fit(X, y)

os.makedirs("model", exist_ok=True)


with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)