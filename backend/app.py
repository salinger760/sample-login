from flask import Flask, Response, request
from flask_cors import CORS
import os, sys, json, logging
import pymysql.cursors

logging.getLogger('flask_cors').level = logging.DEBUG

app = Flask(__name__)
CORS(app, resources={"/auth*": {"origins": "http://localhost:8080"}})


@app.route('/')
def pong():
  return 'Pong'


@app.route('/auth')
def auth():
  flg = False
  uname = request.args.get('username', '')
  upass = request.args.get('password', '')


  conn = pymysql.connect(host='127.0.0.1',
                    user='root',
                    password='password',
                    db='testdb',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor)


  try:
    with conn.cursor() as cursor:
      sql = "SELECT user_id, name FROM users WHERE user_id = %s"
      cursor.execute(sql, ('1',))
      rows = cursor.fetchall()
      print(rows)
  finally:
    conn.close()

  for row in rows:
    if upass == row[0]:
      return json.dumps({"result": "success"})

  return json.dumps({"result": "fail"})