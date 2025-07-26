import requests, time

sample = {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}

url = "http://localhost:8000/predict"
for attempt in range(10):
    try:
        response = requests.post(url, json=sample)
        print("✅ Status Code:", response.status_code)
        print("🌼 Response:", response.json())
        break
    except Exception as e:
        print(f"⏳ Attempt {attempt+1}: API not ready ({e})")
        time.sleep(3)
else:
    print("❌ API not responsive after retries")