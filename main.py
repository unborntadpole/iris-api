from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
import pickle
import numpy as np

# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this later to specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

class IrisRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/predict")
def predict_species(data: IrisRequest):
    input_array = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
    prediction = model.predict(input_array)
    return {"predicted_class": int(prediction[0])}