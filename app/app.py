import os
from flask import Flask, jsonify
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)

from models import City


@app.route('/')
def index():
    return 'Flask is running on Docker!'


@app.route('/data')
def cities():
    data = City.query.all()
    return jsonify(cities = ['{}!'.format(city.name.upper())
        for city in data])


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
