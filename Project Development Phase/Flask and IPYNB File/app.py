from flask import Flask,render_template,request
app=Flask(__name__)
import pickle
import numpy as np
model= pickle.load(open('occupancy.pkl','rb'))
@app.route('/')
def start():
    return render_template("index.html")

@app.route('/login',methods=['POST'])
def login():
    t=request.form['temp']
    h=request.form['humid']
    l=request.form['light']
    c=request.form['co']
    hum=request.form['hr']
    ye=request.form['yr']
    m=request.form['mt']
    d=request.form['dy']
    res=[[float(t),float(h),float(l),float(c),float(hum),float(ye),float(m),float(d)]]
    out=model.predict(res)
    print(out)
    return render_template("index.html", y="The Occupancy Rate is "+str((out[0])))
if __name__== '__main__':
    app.run(debug=False,host='0.0.0.0')



