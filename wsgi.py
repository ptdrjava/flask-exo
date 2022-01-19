# wsgi.py
# pylint: disable=missing-docstring
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World! modif"

@app.route('/api/v1/produits')
def produits():
    return jsonify(PRODUITS = {1:{"id":1,"name":"Skello"},2:{"id":2,"name":"Socialive.tv"}})
