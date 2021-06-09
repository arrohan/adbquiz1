from flask import Flask, render_template, request
import os
app = Flask(__name__)

@app.route('/')
def hello():	
	return "<h1>Hello</h1>"

@app.route('/showFiles',methods=["POST","GET"])
def fileNames():
	path = os.getcwd()
	files = os.listdir(path)
	return render_template('files.html',filenames=files)