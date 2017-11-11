# Udacity - SQL Project - Logs Analysis 

## Overview

This program is designed to analyse data from the newsdata.sql file provided by Udacity [here](http://video.udacity-data.com.s3.amazonaws.com/topher/2016/August/57b5f748_newsdata/newsdata.zip) using a Virtual Machine created using vagrant found [here](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip) to pull relevant data using PostgreSQL.

The Python program was written in Python 2. There are three methods in this program, one for each question asked. Each method connects to the news database. It then executes a SQL command inorder to retrieve the necessary data to answer the question being asked. The results of the SQL command are stored into a variable. The program prints outs a message, displaying the question the method is answering. The store stored results are then looped through using a for loop and the data for each loop is used to display the relevant information in the format specificed by the Udacity [instructions](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/262a84d7-86dc-487d-98f9-648aa7ca5a0f/concepts/b1bc900a-44ea-43e9-a51b-d3313705277f). After looping through the stored data, the database connection is closed. 

The purpose of the analysis is to answer three questions:
  1. What are the most popular three articles of all time?
  2. Who are the most popular article authors of all time?
  3. On which days did more than 1% of requests lead to errors?

## Instructions

1. Install the VM created by Udacity, instructions can be found [here](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0). 
2. Download the newsdata.sql file found [here](http://video.udacity-data.com.s3.amazonaws.com/topher/2016/August/57b5f748_newsdata/newsdata.zip) to the VM. Once the newsdata.sql file is downloaded and uncompressed, it needs to be imported into the news database. Use the command `psql -d news -f newsdata.sql` inorder to call the PostgreSQL command line program, connect to the database named news which has been set up and run the SQL statements in the file newsdata.sql.
3. Download the LogsAnalysisProject.py file to the same location in the VM as your newsdata.sql file. 
4. Using your terminal, locate to the VM where your sql and py files are located. Run: `python LogsAnalysisProject.py` this will print out answers to the questions above.
