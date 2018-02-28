from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo

import scrape_mars as scrape1

app = Flask(__name__)

mongo = PyMongo(app)

@app.route('/scrape')
def scrape():
    data = scrape1.strip()
    return data


@app.route('/')
def index():
	return render_template("index.html")

if __name__ == "__main__":
    app.run()