# FreddiMac
Bootstrap a python application/script that can load at least 1GB of the Freddie Mac Single Family Loan Level Data Set to a database of your choice (preferably in AWS). 

# version
version: python3.9


# Steps That are required to run this script

STEP1:(create virtual environment)
1. Create a project named 'FreddieMac'
2. Create Virtual Environment with 'venv' module 

# Download Source Data
STEP2:(download and extract source dataset)
1. Downloaded data set https://freddiemac.embs.com/FLoan/Data/download.php?f=historical_data_2013&s=1509408608 from https://freddiemac.embs.com/FLoan/Data/downloadA.php
2. Used 4 text files post extraction of each quarterly wise data provided, and stored them in 'historical_data_2013' folder within current working directory.

STEP3:(create script for actual requirement)

1. install 'pandas' framework
2. create dataframe with all the data from *.txt files

STEP4: (create engine using SQLALCHEMY)

# AWS-RDS -Instance

1. You should have AWS Account
2. Create RDS instance(MySQL)
3. create username, Password, database name

# Environment variables

create environment variables for the following

1. AWS ACCESS & SECRET keys
2. RDS instance endpoint, username, password, port, database

# Create database engine to connect to database

1. install 'mysql-connector' package
2. create 'requirements.txt' file and add all dependencies required for this project to run


# Run Script
1. First install all dependencies specified in 'requirements.txt' file
give a command 'pip install -r requirements.txt'
2. go to your project directory 'FreddieMac'
3. give a command 'python3 single-family-loan-data.py' and press enter

The script will run successfully

Thank you.






