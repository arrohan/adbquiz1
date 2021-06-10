from flask import Flask, render_template, request
import os

app = Flask(__name__)
app.secret_key="ABCDEF"


if __name__ == '__main__':
    
  app.run(host='127.0.0.1', port=8080, debug=True)
  app.config['JSON_SORT_KEYS']=False

@app.route('/')
def hello():
	return render_template('index.html')

@app.route('/names', methods=["POST","GET"])
def show_names():
    path=os.getcwd()
    path=path+"/static"
    files=os.listdir(path)
    return render_template('index.html',fn=files)