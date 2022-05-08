import pickle
lr2 = pickle.load(open("lr_c32_TD.pkl",'rb'))

import numpy as np
from flask import Flask,request,jsonify,render_template

app = Flask(__name__)
@app.route("/")# It binds the website with a specific url 

def homepage(name):
    return render_template("index.html")    
 
@app.route("/predict", method = ['POST']  ) 
def predict(name):
    int_features = lr.predict([np.array([int(x) for x in reuqest.form.values()])])
    return render_template("index.html", prediction_text = int_features)    
   
if __name__=="__main__":
    app.run(port = 5001, debug = True)