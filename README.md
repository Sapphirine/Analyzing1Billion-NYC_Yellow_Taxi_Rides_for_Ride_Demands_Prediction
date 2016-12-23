# Analyzing1Billion-NYC_Yellow_Taxi_Rides_for_Ride_Demands_Prediction
Team ID: 201612-101 Big Data Analytics Fall 2016 Final Project 

## How to use this code
All source code are in src/ dirctory. There're mainly three parts: model code, processingData code and also webApp code. Code in processingData/ is used for processing raw data to the format which our module can use. Our model is in model/ dir, which is a python random forest model code. Finally, after processed data and trained the model, a AWS based website is built. Those code are in webApp.

## How to visit this web app
Go to http://www.teximap.com.s3-website-us-east-1.amazonaws.com/ webpage. Choose the pick up location as well as pick up time. You'll get the prediction result by using our model in the backend.

Have fun
