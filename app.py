from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["todoapp"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api')
def api():
    data = {"message": "Hello from API", "status": "success"}
    return jsonify(data)

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    item_name = request.form.get('itemName')
    item_description = request.form.get('itemDescription')
    db.todos.insert_one({
        "itemName": item_name,
        "itemDescription": item_description
    })
    return jsonify({"message": "Item saved!", "status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
