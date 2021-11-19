##################################################################
## IPK API kelompok D2 dan D3 sudah dideploy diheroku.          ##
## file Procfile digunakan untuk keperluan deployment ke heroku ## 
## Disini kami menggunkan gunicorn webserver                    ##
## web server gate menggunakan model WSGI                       ##
##################################################################

# API endpoint
# https://api-d2d3.herokuapp.com/ipk/data -> POST request
# https://api-d2d3.herokuapp.com/ipk/baru -> GET request


# import flask library
import flask
from flask import request, jsonify
import json

# datetime untuk mengambil local current time
from datetime import datetime

# Membuat aplikasi server flask
app = flask.Flask(__name__)

# List kosong untuk menampung data hasil POST request
data = []

# Routing untuk GET request semua data ipk
@app.route('/ipk/data', methods=['GET'])
def ipk_data():
    # Mengembalikan data dalam bentuk json
    return jsonify(data)

# Routing untuk POST request pengiriman data ipk
@app.route('/ipk/baru', methods=['POST'])
def update_record():
    # Menerima data hasil request dalam bentuk json
    record = json.loads(request.data)

    # Menambahkan nilai current time ketika menerima data
    record['time'] = datetime.now().strftime('%H:%M:%S')

    # Data dimasukkan ke dalam list
    data.append(record)

    # Mengembalikan data yang di post dalam bentuk json
    return jsonify(record)
