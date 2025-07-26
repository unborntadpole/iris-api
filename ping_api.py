import requests

try:
    sample = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2
    }

    response = requests.post("http://localhost:8000/predict", json=sample)
    print("Status Code:", response.status_code)
    print("Response:", response.json())
except Exception as e:
    print("Failed to reach API:", e)