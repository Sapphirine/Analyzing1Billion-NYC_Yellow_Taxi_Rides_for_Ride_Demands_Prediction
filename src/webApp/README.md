# Yellow Taxi Prediciton Website 
This website is design and built for big daya analysis project. The whole structure is build in AWS cloud service.
## Front End
The front end of the web mainly used AngularJS for developing. Google Map API and Open Weather API are also used for map display and weather prediction.
Index.html file is the front-end display file, and AngularJS controller file is maps.js. They are all stored in AWS S3 Bucket so that it can be easily reached from browser. 
## Swegger File
URL mapping from front end to back end is in Swagger file Swagger.json. Which defines the rule for sending request from front page to AWS Lambda Function.
## AWS Lambda Function
Back End program is in this part. After getting request with other information (like weather, time and location), back end file would predict the riding number around this place in this hour. The result will send back to front end.
