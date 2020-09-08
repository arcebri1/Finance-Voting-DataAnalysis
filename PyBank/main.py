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
#csvheader = next(reader)
#budget = {}

#for row in reader:
    #{'Date': row[0], 'Profit/Losses':row[1]}
    #print(row[0])
    #months=len(reader)
    #print(months)

#import csv

#total_months = 0
#total_profit_and_losses = 0



#with open('C:\\Users\\loren\\Desktop\\python-challenge\\PyBank\\Resources\\budget_data.csv', 'r') as csvfile:
    #reader = csv.DictReader(csvfile)
    

    #for row in reader:
        #total_months = total_months + 1
        #total_profit_and_losses = total_profit_and_losses + int(row['Profit/Losses'])
        #count = count + 1
        
        #average_change = profits - past_profits
#print(total_months)
#print(total_profit_and_losses)
#print(average_change)

import os
import csv

total_months = 0
total_profit_and_losses = 0
past_profit_loss = 0
profit_and_loss_change = 0
changes = []
greatest_increase_profits = ['', 0]
greatest_decrease_losses = ['', 9999999]


with open('C:\\Users\\loren\\Desktop\\python-challenge\\PyBank\\Resources\\budget_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    

    for row in reader:
    
        total_months = total_months + 1
        #print(total_months)
        total_profit_and_losses = total_profit_and_losses + int(row['Profit/Losses'])
        #print(total_profit_and_losses)
        profit_and_loss_change = int(row['Profit/Losses']) - past_profit_loss
        #print(profit_and_loss_change)
        past_profit_loss = int(row['Profit/Losses'])
        #print(past_profit_loss)

        if profit_and_loss_change > greatest_increase_profits[1]:
            greatest_increase_profits[1]= profit_and_loss_change
            greatest_increase_profits[0]= row['Date']

        if profit_and_loss_change < greatest_decrease_losses[1]:
            greatest_decrease_losses[1] = profit_and_loss_change
            greatest_decrease_losses[0] = row['Date']
        changes.append(int(row['Profit/Losses']))
        #print(average_change)
    average_change = sum(changes)/len(changes)
print(total_months)
print(total_profit_and_losses)
#print(average_change)
#print(months)
#print(profit_and_loss_change)
print(str(round(sum(changes) / len(changes),2)))
print(str(greatest_increase_profits[0]))
print(str(greatest_increase_profits[1]))
print(str(greatest_decrease_losses[0]))
print(str(greatest_decrease_losses[1]))