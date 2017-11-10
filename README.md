# Udacity - SQL Project - Logs Analysis 

## Overview

This program is designed to analyse data from the newsdata.sql file provided by Udacity [here](http://video.udacity-data.com.s3.amazonaws.com/topher/2016/August/57b5f748_newsdata/newsdata.zip) using a Virtual Machine created using vagrant found [here](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip) to pull relevant data using PostgreSQL.

The Python program was written in Python 2. 

The purpose of the analysis is to answer three questions:
  1. What are the most popular three articles of all time?
  2. Who are the most popular article authors of all time?
  3. On which days did more than 1% of requests lead to errors?

## Instructions

1. Install the VM created by Udacity, instructions can be found [here](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0). 
2. Download the newsdata.sql file found [here](http://video.udacity-data.com.s3.amazonaws.com/topher/2016/August/57b5f748_newsdata/newsdata.zip) to the VM.
3. Download the LogsAnalysisProject.py file to the same location in the VM as your newsdata.sql file. 
4. Using your terminal, locate to the VM where your sql and py files are located. Run: `python LogsAnalysisProject.py` this will print out answers to the questions above.
