import uvicorn
from fastapi import FastAPI, Form
import requests

COMPOSITION_URL = "http://0.0.0.0:8080/composition/"

app = FastAPI()

@app.post("/submit")
async def submit_form(login: str = Form(...), password: str = Form(...)):
    resp = requests.request("POST", COMPOSITION_URL, json={"login": login, "password": password})
    return resp.json()

if __name__ == "__main__":
    uvicorn.run(host="0.0.0.0", port=8081, app=app)