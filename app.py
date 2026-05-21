import os
from flask import Flask, send_from_directory

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def home():
    file_path = os.path.join(BASE_DIR, "lativm_output.html")
    if os.path.exists(file_path):
        return send_from_directory(BASE_DIR, "lativm_output.html")
    return "LATIVM AI сеуште генерира содржина...", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)