from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello():
	return "<h1>Hello</h1>"
