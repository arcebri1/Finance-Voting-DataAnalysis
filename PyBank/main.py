#import the module and module to read the csv file
import os
import csv

#declare variable
total_months = 0
total_profit_and_losses = 0
past_profit_loss = 0
profit_and_loss_change = 0
changes = []
greatest_increase_profits = ['', 0]
greatest_decrease_losses = ['', 9999999]

#path to collect data from csv file
budget_csv = os.path.join('C:\\Users\\loren\\Desktop\\python-challenge\\PyBank\\Resources\\budget_data.csv')

#open the csv, make sure it is split/read by the correct delimiter: ,
with open (budget_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#need to skip header row
    csvheader = next(csvfile)

#loop through the data
    for row in csvreader:
        
        total_months = total_months + 1
        total_profit_and_losses = total_profit_and_losses + int(row[1])
        profit_and_loss_change = int(row[1]) - past_profit_loss
        past_profit_loss = int(row[1])

        if profit_and_loss_change > greatest_increase_profits[1]:
            greatest_increase_profits[1]= profit_and_loss_change
            greatest_increase_profits[0]= (row[0])

        if profit_and_loss_change < greatest_decrease_losses[1]:
            greatest_decrease_losses[1] = profit_and_loss_change
            greatest_decrease_losses[0] = (row[0])
        changes.append(int(row[1]))

print('Financial Analysis')
print("--------------------")
print(total_months)
print(total_profit_and_losses)
print(str(round(sum(changes) / len(changes))))
print(str(greatest_increase_profits[0]))
print(str(greatest_increase_profits[1]))
print(str(greatest_decrease_losses[0]))
print(str(greatest_decrease_losses[1]))


#Naming the path of the text file to write the results in
output_file = os.path.join('C:\\Users\\loren\\Desktop\\python-challenge\\PyBank\\analysis\\results.txt')

#Open the file to write on it and command it to write each result you want. Remember to use \n to move to the next line
with open(output_file, "w") as text:
    
    text.write('Financial Analysis\n')
    text.write('-----------------------\n')
    text.write(f'Total Months: {total_months}\n')
    text.write(f"Total: ${total_profit_and_losses}\n ")
    text.write(f"Average Change: ${sum(changes) / len(changes):.2f}\n ")
    text.write(f"Greatest Increase in Profits: {greatest_increase_profits[0]} (${greatest_increase_profits[1]})\n ")
    text.write(f"Greatest Decrease in Profits: {greatest_decrease_losses[0]} (${greatest_decrease_losses[1]})\n ")
  




    
