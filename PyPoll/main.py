#import os
#import csv

#total_votes = 0

#with open('C:\\Users\\loren\\Desktop\\python-challenge\\PyPoll\\Resources\\election_data.csv', 'r') as csvfile:
    #reader = csv.DictReader(csvfile)
    

    #for row in reader:
        #print(row)
        #total_votes = total_votes + 1
        #print(total_votes)

#import module
import os
#import module to read csv files
import csv

#declare variable
total_votes = 0

#path to collect data from excel file
#election_csv = os.path.join('python-challenge/PyBank/Resources/budget_data.csv')
election_csv = os.path.join('C:\\Users\\loren\\Desktop\\python-challenge\\PyPoll\\Resources\\election_data.csv')

#open the csv
with open (election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)

#skip header row first
    csvheader = next(csvreader)
    print(f'csv header: {csvheader}')

#read each row after the header
    #for row in csvreader:
        #print(row)