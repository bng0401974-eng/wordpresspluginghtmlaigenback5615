# app.py
import os
from flask import Flask, send_file

app = Flask(__name__)

# Патека до твојот генериран HTML фајл
OUTPUT_FILE = "lativm_output.html"

@app.route('/')
def home():
    # Провери дали фајлот постои
    if os.path.exists(OUTPUT_FILE):
        return send_file(OUTPUT_FILE)
    else:
        return "LATIVM AI сеуште генерира содржина... почекај малку.", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)