
from flask import (
    Flask,
    request
)

app = Flask(__name__)

from app.database import data_types

RESPONSE = {
    "status": "ok",
}

@app.get("/data_types")
def index():
    response = dict(RESPONSE)
    response["data_type"] = data_types.scan()
    return response

@app.get("/data_types/integers")
def integers():
    response = dict(RESPONSE)
    response["data_type"] = data_types.select_by_type(name="Integer")
    return response

@app.get("/data_types/floats")
def floats():
    response = dict(RESPONSE)
    response["data_type"] = data_types.select_by_type(name="Float")
    return response

@app.get("/data_types/booleans")
def bools():
    response = dict(RESPONSE)
    response["data_type"] = data_types.select_by_type(name="Boolean")
    return response

@app.get("/data_types/strings")
def strings():
    response = dict(RESPONSE)
    response["data_type"] = data_types.select_by_type(name="String")
    return response

@app.get("/data_types/lists")
def lists():
    response = dict(RESPONSE)
    response["data_type"] = data_types.select_by_type(name="List")
    return response

@app.get("/data_types/dictionaries")
def dictionaries():
    response = dict(RESPONSE)
    response["data_type"] = data_types.select_by_type(name="Dictionary")
    return response

@app.get("/data_types/tuples")
def tuples():
    response = dict(RESPONSE)
    response["data_type"] = data_types.select_by_type(name="Tuple")
    return response

@app.post("/data_types")
def create_data_type():
    dt_body = request.json
    data_types.create(dt_body)
    return "", 204

@app.put("/data_types/<int:pk>")
def update_data_type(pk): # pk = primary key (_id column), because "id" is taken in python3
    dt_body = request.json
    data_types.update(dt_body, pk)
    return "", 204

@app.delete("/data_types/<int:pk>")
def delete_data_type(pk): # pk = primary key
    data_types.delete(pk)
    return "", 204
