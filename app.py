'''
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/contatos")
def user():
    return render_template("contato.html")

@app.route("/quemsomos")
def who():
    return render_template("sobre.html")

'''