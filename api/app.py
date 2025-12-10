from flask import Flask, render_template, send_from_directory
import os

# IMPORTANT: adjust paths because app.py is inside /api/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory(os.path.join(STATIC_DIR, 'images'), filename)

# Vercel does not use debug mode or manual port binding.
def handler(event, context):
    return app(event, context)

if __name__ == '__main__':
    app.run()
