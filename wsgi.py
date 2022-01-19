# wsgi.py
# pylint: disable=missing-docstring
from asyncio.windows_events import NULL
from flask import Flask, jsonify, abort

app = Flask(__name__)

data = [{"id":1,"name":"Skello"},{"id":2,"name":"Socialive.tv"},{"id":3,"name":"sup"}]

@app.route('/')
def hello():
    return "Hello World! modif"

@app.route('/api/v1/products')
def produits():
    return jsonify(data)

# @app.route('/api/v1/products/<id>')
# def produit_by_id(id):
#     result = ""
#     for var in data:
#         id_in_data=var["id"]
#         if id_in_data == int(id):
#             result = var
#             break
#     if result == "":
#         abort(404)
    
#     return jsonify(result)
