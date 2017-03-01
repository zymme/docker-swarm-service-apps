#!/usr/local/bin/python
from flask import Flask, jsonify, abort
from flask import make_response
from flask import request
from dropmsg import drop_message
from pymongo import MongoClient
from bson.json_util import dumps
from bson import json_util
from flask_cors import CORS, cross_origin


import json


# ******* Memory messages data  ********

messages = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'Person': 'Dave Z',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': 'false'
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'Person': 'Dave Z',
        'description': u'Need to find a good Python tutorial on the web',
        'done': 'false'
    }
]

# **********************************************

app = Flask(__name__)
CORS(app)


@app.route('/messaging/api/v1.0/messages', methods=['GET'])
def get_messages():

    client = MongoClient("mongodb://localhost:27017")
    db = client.mydb

    result = db.messaging.find()

    json_docs = []
    for doc in result:
        json_doc = json.dumps(doc, default=json_util.default)
        json_docs.append(json_doc)


    print("results from mongo find() {}".format(result))

    return jsonify({'messages': json_docs})


@app.route('/messaging/api/v1.0/messages/<int:message_id>', methods=['GET'])
def get_message(message_id):

    message = [message for message in messages if message['id'] == message_id]
    if len(message) == 0:
        abort(404)
    return jsonify({'message': message[0]})


@app.route('/messaging/api/v1.0/messages', methods=['POST'])
def create_message():

    print("In POST for messages")
    print(request.json)

    #print(request.json['message']['title'])

    if not request.json:
        abort(400)

    if 'title' not in request.json['message']:
        abort(400)

    message = {
        'title': request.json['message']['title'],
        'description': request.json['message']['description'],
        'done': 'false',
        'to': request.json['message']['to']
    }

    drop_message(message)

    return jsonify({'message': message}), 201






@app.route('/')
def index():
    return "Hello, World! This is a simple messaging API"


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
