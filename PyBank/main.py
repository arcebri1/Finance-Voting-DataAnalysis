#import os

#cwd = os.getcwd()  # Get the current working directory (cwd)
#files = os.listdir(cwd)  # Get all the files in that directory
#print("Files in %r: %s" % (cwd, files))




#import module
import os
#import module to read csv files
import csv

#path to collect data from excel file
#budget_csv = os.path.join('python-challenge/PyBank/Resources/budget_data.csv')
budget_csv = os.path.join('C:\\Users\\loren\\Desktop\\python-challenge\\PyBank\\Resources\\budget_data.csv')

#open the csv
with open (budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
