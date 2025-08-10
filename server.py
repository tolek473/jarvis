from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__, template_folder='templates')

@app.route('/')
def dashboard():
    return render_template('dashboard.html', time=datetime.now())

@app.route('/api/hello')
def hello():
    return {"message": "Cześć, tu Jarvis!"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
