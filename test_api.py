from fastapi.testclient import TestClient
from main import app

# import sys

client = TestClient(app)

def test_prediction():
    sample = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }
    response = client.post("/predict", json=sample)
    assert response.status_code == 200
    assert "predicted_class" in response.json()
    return response.json()["predicted_class"]

if __name__ == "__main__":
    prediction = test_prediction()
    print("Predicted class:", prediction)
    print("Test completed.")