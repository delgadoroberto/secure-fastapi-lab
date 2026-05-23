from fastapi import FastAPI
import pickle
import base64

app = FastAPI(debug=True)

API_TOKEN = "SUPER-TOP-SECRET-TOKEN"

@app.get("/")
def home():
    return {"message": "Vulnerable FastAPI App"}

@app.get("/deserialize")
def deserialize(data: str):

    decoded = base64.b64decode(data)

    obj = pickle.loads(decoded)

    return {"object": str(obj)}
