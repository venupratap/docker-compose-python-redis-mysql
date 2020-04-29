from typing import List, Dict
from flask import Flask
import mysql.connector
from reids import Redis
import json

app = Flask(__name__)
redis = Redis(host='redis', port=6379)


def favorite_colors() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'knights'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM favorite_colors')
    results = [{name: color} for (name, color) in cursor]
    cursor.close()
    connection.close()

    return results

@app.route('/')
def index() -> str:
    return json.dumps({'favorite_colors': favorite_colors()})
def hello():
    redis.incr('hits')
    return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=true)
