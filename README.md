# flaskapp_myob

[![Build Status](https://travis-ci.org/maheshmarri/flaskapp_myob.svg?branch=master)](https://travis-ci.org/maheshmarri/flaskapp_myob)

# Intro
This is simple flask application based on Python Flask Web framework which utilizes 
the app routes view functions as endpoints.

App has three endpoints ,default,/health and /metadata
/
    default 
/health 
    would show status_code and message.
/metadata 
    Would show application metadata,version  and github last commit.  


# UnitTest
I have used python unittest framework to develop the unit test cases for the above app to test 
endpoints and its data.

`python test.py -v`

# CI/CD 
Configured Travis as CI/CD Pipeline for each commit on github. And also app to be built on python version 2.7 and 3.6.
So for each commit of the 2 parallel builds running for each of the python version.

# Depndencies
I have packaged dependencies in requirement.txt file to install dependencies using pip before the app would
executed.


# Docker Build
Containerized the flask app into single deployable artifact and its dependencies.

`docker build -t flaskapp:latest .`

# Running Flask Docker Container
`docker run -d -p 80:80 flaskapp`

# App Sreenshots

