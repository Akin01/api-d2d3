import flask
from flask import request, jsonify, abort
import json
from datetime import datetime

app = flask.Flask(__name__)
app.config["DEBUG"] = True

data = [
    {
        "id": 1,
        "nama": "Yosa",
        "ipk": 3.72
    },
    {
        "id": 2,
        "nama": "yazid",
        "ipk": 3.61
    }
]

@app.route('/api/ipk/data', methods=['GET'])
def ipk_data():
    return jsonify(data)

@app.route('/api/ipk', methods=['GET'])
def ipk_nama():

    ipk_get_name = request.args['nama']

    if not len(data):
        return jsonify(data)

    for mahasiswa in data:
        if mahasiswa['nama'].lower() == ipk_get_name.lower():
            return jsonify(mahasiswa)
        elif not ipk_get_name:
            return "Masukkan query dengan benar!!!"
        
    abort(404, description="IPK not found")


@app.route('/api/ipk/baru', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    record['time'] = datetime.now().strftime('%H:%M:%S')

    if not len(data):
        data.append(record)
        return jsonify(record)
    
    for mahasiswa in data:
        if mahasiswa['id'] == record['id']:
            return "id forbidden!!!"

    data.append(record)
    return jsonify(record)
