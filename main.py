from flask import Flask, render_template, redirect, url_for, flash, jsonify
from datetime import datetime, timedelta
import pandas as pd
app = Flask(__name__)

data = pd.read_csv("data.csv")

@app.route('/')
def home():
  return render_template("index.html", data=data, length=len(data[data.Day == "Monday"].Class.value_counts().index.tolist()))

@app.route("/gettime")
def gettime():
    time = datetime.now().strftime("%A, %B %d, %Y, %I:%M:%S %p")
    return jsonify({"Content": time})
app.run(host='0.0.0.0', port=5000, debug=True)