#import module
import os
#import module to read csv files
import csv

#path to collect data from excel file
budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')

#open the csv
with open (budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    