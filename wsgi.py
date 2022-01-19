# wsgi.py
# pylint: disable=missing-docstring
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World! modif"

@app.route('/api/v1/products')
def produits():
    return jsonify([{"id":1,"name":"Skello"},{"id":2,"name":"Socialive.tv"},{"id":3,"name":"sup"}])
