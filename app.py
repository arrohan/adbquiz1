from flask import Flask, render_template, request
import os
import csv
import pandas as pd
import numpy as np

app = Flask(__name__)
app.secret_key="ABCDEF"


if __name__ == '__main__':
    
  app.run(host='127.0.0.1', port=8080, debug=True)
  app.config['JSON_SORT_KEYS']=False

df=pd.read_csv('names.csv')
df1=df.replace(np.nan, '', regex=True)
data=df1.values.tolist()

@app.route('/')
def hello():
	return render_template('index.html')

@app.route('/names', methods=["POST","GET"])
def show_names():
    path=os.getcwd()
    path=path+"/static"
    files=os.listdir(path)
    return render_template('filenames.html',fn=files)

@app.route('/room', methods=["POST","GET"])
def show_details():
    df=pd.read_csv('names.csv')
    print(df)
    df1=df.replace(np.nan, '', regex=True)
    data=df1.values.tolist()
    print(data)
    room=request.form.get("roomnumber")
    room2=int(room)

    people=[]
    count=0
    for i in data:
        if(i[2]!="" and i[2]!=" "):
            rn=float(i[2])
            rn1=int(i[2])
            if(rn1==room2):
                print(count)
                count=count+1
                people.append(i)
    
    return render_template('roomdetails.html',list1=people)


