import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))  # Default to 8080 if PORT not set
    app.run(host='0.0.0.0', port=port)
