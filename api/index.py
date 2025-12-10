from flask import Flask, render_template, send_from_directory
import os

# Absolute paths because this file is inside /api
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")

app = Flask(
    __name__,
    template_folder=TEMPLATE_DIR,
    static_folder=STATIC_DIR
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory(STATIC_DIR, filename)

@app.route("/images/<path:filename>")
def images(filename):
    return send_from_directory(os.path.join(STATIC_DIR, "images"), filename)

# IMPORTANT: No debug, no port, no handler
if __name__ == "__main__":
    app.run()
