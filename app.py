from fastapi import FastAPI
import pickle
import base64
import os

app = FastAPI(debug=False)

API_TOKEN = os.getenv("API_TOKEN")

@app.get("/")
def home():
    return {"message": "Vulnerable FastAPI App"}

@app.get("/deserialize")
def deserialize():
    return {"message": "Deserialization disabled"}
