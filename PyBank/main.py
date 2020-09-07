#import os

#cwd = os.getcwd()  # Get the current working directory (cwd)
#files = os.listdir(cwd)  # Get all the files in that directory
#print("Files in %r: %s" % (cwd, files))




#import module
#import os
#import module to read csv files
#import csv

#path to collect data from excel file
#budget_csv = os.path.join('python-challenge/PyBank/Resources/budget_data.csv')
#budget_csv = os.path.join('C:\\Users\\loren\\Desktop\\python-challenge\\PyBank\\Resources\\budget_data.csv')

#open the csv
#with open (budget_csv) as csvfile:
    #csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)

#read header row first
    #csvheader = next(csvreader)
    #print(f'csv header: {csvheader}')

#read each row after the header
    #for row in csvreader:
        #print(row)

#import csv

#f = open('C:\\Users\\loren\\Desktop\\python-challenge\\PyBank\\Resources\\budget_data.csv', 'r')

#reader = csv.reader(f)

#budget = {}

#for row in reader:
    #{'Date': row[0], 'Profit/Losses':row[1]}
    #print(row)

import csv

total_months = 0
total_profit_and_losses = 0

with open('C:\\Users\\loren\\Desktop\\python-challenge\\PyBank\\Resources\\budget_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        #total_months = total_months + 1
        total_profit_and_losses = total_profit_and_losses + int(row['Profit/Losses'])
#print(total_months)
print(total_profit_and_losses)






