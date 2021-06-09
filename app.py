from flask import Flask, render_template, request
import os
app = Flask(__name__)

@app.route('/')
def hello():	
	render_template('index.html')

@app.route('/showFiles',methods=["POST","GET"])
def fileNames():
	path = os.getcwd()
	files = os.listdir(path)
	render_template("files.html",filenames=files)