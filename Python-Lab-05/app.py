from flask import Flask, render_template, request
import pickle as pkl
import numpy as np

# read the pickle
rf_model = pkl.load(open('model.pkl', 'rb'))

#initialize the flask app
app = Flask(__name__)

# Route for rendering 'index.html' file
@app.route('/', methods = ['GET'])
def home():
    return render_template('index.html')

# Route for predicting the outcome with the help of model created
@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    Present_Price = float(request.form['Present_Price'])
    Kms_Driven = int(request.form['Kms_Driven'])
    Owner = int(request.form['Owner'])
    Fuel_Type = int(request.form['Fuel_Type'])
    Age_of_the_car = int(request.form['Age_of_the_car'])
    Seller_Type = int(request.form['Seller_Type'])
    Transmission = int(request.form['Transmission'])
    
    # Make prediction
    prediction = rf_model.predict([[ Present_Price, Kms_Driven, Owner, Fuel_Type,Age_of_the_car, Seller_Type, Transmission]])
    
    # Display prediction on index.html
    return render_template('index.html', prediction_text='Predicted Selling Price: {:.2f} lakhs'.format(prediction[0]))


if __name__ == "__main__":
    app.run(debug=True)
