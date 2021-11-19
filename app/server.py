import flask
from flask import request, jsonify
import json
from datetime import datetime

app = flask.Flask(__name__)

data = []

@app.route('/ipk/data', methods=['GET'])
def ipk_data():
    return jsonify(data)

@app.route('/ipk/baru', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    record['time'] = datetime.now().strftime('%H:%M:%S')

    if not len(data):
        data.append(record)
        return jsonify(record)

    data.append(record)
    return jsonify(record)
