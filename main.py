import sys
from flask import Flask, json, request, current_app
from src.controllers.main_controller import *

app = Flask(__name__)

rp = ''
with app.test_client() as client:
    client.get('/')
    rp = request.path

@app.route('/', methods=['GET'])
def get_main():
    return request.url 

print(get_main)

if __name__ == '__main__':
    app.run(debug=True, port=5000)