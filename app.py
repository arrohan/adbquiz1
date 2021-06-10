from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import os

df = pd.read_csv('names.csv')
df1=df.replace(np.nan,"",regex=True)

data = df1.values.tolist()

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
	return render_template('names.html',fn=files)
