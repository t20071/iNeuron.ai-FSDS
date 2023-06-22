import pickle
from flask import Flask,app,jsnoify
import numpy as np
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/predict_api',methods = ['POST'])
def predict_api():

    data = request.json['data']
    print(data)
    new_data = [list(data.values())]
    output = model.predict(new_data)[0]
    return jsnoify(output)

if __name__ == "__main__":
    app.run(debug = True)

## loading a pickle file