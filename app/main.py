import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import json
import ast


app = FastAPI()

@app.get("/")
def home():
    return {"Hello" : "World"}

@app.post("/onesum")
def sum_plus_one(x : int):
    return x + 1

@app.post("/listtodict")
def to_dict_from_tuple(lst : str):
    print("Before conversion: ", lst)
    lst = ast.literal_eval(lst)
    if type(lst) != list or len(lst) < 2:
        return json.dumps({"Error" : "Tuple must be of length two or greater"})
    else:
        return {lst[0] : lst[1]}