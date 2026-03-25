from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import json, os

app = Flask(_name_)
client = MongoClient("mongodb://localhost:27017/")
db = client["todo_db"]
collection = db["todos"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api')
def api():
    with open('data/api_data.json') as f:
        return jsonify(json.load(f))

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    data = request.json
    collection.insert_one({"itemName": data.get('itemName'), "itemDescription": data.get('itemDescription')})
    return jsonify({"message": "Saved!"}), 201

if _name_ == '_main_':
    app.run(debug=True)
