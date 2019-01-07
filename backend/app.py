from flask import Flask, Response, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={"/auth*": {"origins": "http://localhost:8080"}})

@app.route('/')
def pong():
  return 'Pong'


@app.route('/auth')
def auth():
  return 'hogehoge'