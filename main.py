import pandas as pd
from flask import Flask,jsonify,request
from data import data
api=Flask(__name__)

@api.route("/")
def index():
    name = request.args.get("name")
    planet_data= next(item for item in data if item["name"]==name)
    return jsonify({
        "data":data,
    }),200
api.run(debug=True)