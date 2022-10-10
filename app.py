from flask import Flask, render_template, jsonify, request
import random

template = [
    {
        "inputs":"5",
        "category":"Sports",
        "word":"Chess"
    },
    {
        "inputs":"6",
        "category":"Europeon Country Name",
        "word":"France"
    }
]

app = Flask("__name__")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get-template")
def get_template():
    return jsonify({
        "status":"success",
        "word": random.choice(template)
    })