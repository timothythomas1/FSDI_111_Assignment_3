from flask import (
    Flask,
    render_template, 
    request
) 

import requests

app = Flask(__name__)

BACKEND_URL = "http://127.0.0.1:5004/data_types"

@app.get("/")
def get_index():
    response = requests.get(BACKEND_URL)
    scan_data = response.json().get("data_type")
    return render_template("main.html", data_types=scan_data)

@app.route("/about")
def about():
    me = {
        "first_name": "Tim",
        "last_name": "Tom",
        "Hobbies": "DIY stuff and coding",
        "bio": "My name is Tim Tom, and I am student."
    }
    return render_template("about.html", about_dict = me)

@app.route("/summary")
def summary():
    response = requests.get(BACKEND_URL)
    scan_data = response.json().get("data_type")
    return render_template("summary.html", data_types=scan_data)

@app.get("/floats")
def get_float_page():
    url = "%s/%s" % (BACKEND_URL, "floats")
    response = requests.get(url)
    float_data = response.json().get("data_type")
    return render_template("floats.html", data_type=float_data[0])

@app.get("/booleans")
def get_boolean_page():
    url = "%s/%s" % (BACKEND_URL, "booleans")
    response = requests.get(url)
    boolean_data = response.json().get("data_type")
    return render_template("booleans.html", data_type=boolean_data[0])

@app.get("/integers")
def get_integer_page():
    url = "%s/%s" % (BACKEND_URL, "integers")
    response = requests.get(url)
    integer_data = response.json().get("data_type")
    return render_template("integers.html", data_type=integer_data[0])

@app.get("/strings")
def get_string_page():
    url = "%s/%s" % (BACKEND_URL, "strings")
    response = requests.get(url)
    string_data = response.json().get("data_type")
    return render_template("strings.html", data_type=string_data[0])

@app.get("/lists")
def get_list_page():
    url = "%s/%s" % (BACKEND_URL, "lists")
    response = requests.get(url)
    list_data = response.json().get("data_type")
    return render_template("lists.html", data_type=list_data[0])

@app.get("/dictionaries")
def get_dictionary_page():
    url = "%s/%s" % (BACKEND_URL, "dictionaries")
    response = requests.get(url)
    dictionary_data = response.json().get("data_type")
    return render_template("dictionaries.html", data_type=dictionary_data[0])

@app.get("/tuples")
def get_tuple_page():
    url = "%s/%s" % (BACKEND_URL, "tuples")
    response = requests.get(url)
    tuples_data = response.json().get("data_type")
    return render_template("tuples.html", data_type=tuples_data[0])

# Createing a means to render a form
@app.get("/create/data_types")
def create_data_types_form():
    return render_template("new.html")

@app.post("/create/data_types")
def create_data_type():
    form_data = request.form
    new_dt = {
        "name": form_data.get("name"),
        "summary": form_data.get("summary"),
        "description": form_data.get("description")
    }
    response = requests.post(BACKEND_URL, json=new_dt)
    if response.status_code == 204:
        return render_template("new_success.html")
    else:
        return render_template("failed.html")
