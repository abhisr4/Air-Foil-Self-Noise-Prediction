# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 10:09:39 2020

@author: Abhinaba
"""


from flask import Flask,render_template,redirect,request
import numpy as np
import tensorflow as tf
import pandas as pd

#__name__==__main__
app=Flask(__name__)

@app.route('/')
def homePage():
    return render_template("index.html")

@app.route('/home')
def returnHome():
    return redirect('/')

#want to know the statistical info of the dataset
    
@app.route('/search',methods=['POST'])
def searchInfo():
    if request.method=='POST':
        df=pd.read_csv("Info.csv")
        values=df.drop(['Unnamed: 0'],axis=1)
        values=values.round(decimals=3)
        cols=values.columns
        dfArray=np.asarray(values)
        x=df['Unnamed: 0']
        rows=np.asarray(x)
        #return render_template("index.html",informatonTable=[df.to_html(classes="data")],titles=df.columns.values)
        return render_template("index.html",connected=True,informationTable=dfArray,rows=rows, cols=cols)

#on submit of data requsted by user
@app.route('/submit',methods=['POST'])
def submitData():
    if request.method=='POST':
        #load input parameters from the user and normalise them
        frequency=float(request.form['frequency'])
        AngleOfAttack=float(request.form['AngleOfAttack'])
        chordLength=float(request.form['chordLength'])
        freeSteamVelocity=float(request.form['freeSteamVelocity'])
        suctionSideDisplacement=float(request.form['suctionSideDisplacement'])
        
        #normalisation logic (min max logic)
        f=(frequency-200.0)/(20000.0-200.0)
        a=(AngleOfAttack-0.0)/(22.2-0.0)
        c=(chordLength-0.025)/(0.305-0.025)
        f=(freeSteamVelocity-31.7)/(71.3-31.7)
        s=(suctionSideDisplacement-0.0)/(0.058-0.0)
        
        
        #create a numpy array to pass in the annmodel
        inputParameters=np.array([[f,a,c,f,s]])
        
        
        #load the model
        annModel=tf.keras.models.load_model("ANN_Model")
         
        #predict the output, output will be in numpy array format
        predicted_output=annModel.predict(inputParameters)
        output=[frequency,AngleOfAttack,chordLength,freeSteamVelocity,suctionSideDisplacement,predicted_output[0][0]]
        return render_template("index.html",predictedOutput=output)

if __name__=="__main__":
    app.run(debug=False)