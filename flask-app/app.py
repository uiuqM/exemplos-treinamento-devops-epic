# app.py
from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)

color = os.environ.get('APP_COLOR')

@app.route('/')
def home():
    return render_template('index.html', color=color)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")