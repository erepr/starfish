import uvicorn
from fastapi import FastAPI, Body, Depends
from typing import Optional
import pandas as pd

app = FastAPI()

@app.get("/items/{file_id}")
def read_item(file_id: str):
    url = "http://localhost/v1/storage/files/" + file_id + "/view?project=61908477ab4eb" 
    df = pd.read_csv(url)
    return {"Statistics": df.describe()} 