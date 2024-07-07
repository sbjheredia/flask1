from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def task2():
    return '<p>Zack L. : radar</p><p>Maria S. : lmao'

@app.route('/jesse')
def task3():
    return render_template('jesse.html')
