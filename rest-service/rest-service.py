from flask import Flask, request, jsonify

import db

app = Flask(__name__)

@app.route('/notes', methods = ['POST'])
def create_note():
    data = request.get_json()
    print(data)
    values = (data['name'], data['description'])
    db.create_note_in_db(values)
    return '', 200

@app.route('/notes', methods = ['GET'])
def get_notes():
    result = db.get_notes_from_db()
    # return result
    return jsonify(result)

@app.route('/notes/<id>', methods = ['GET'])
def get_note_by_id(id):
    result = db.get_note_by_id_from_db(id)
    return jsonify(result)
# flask run
# pip install -r requirements.txt