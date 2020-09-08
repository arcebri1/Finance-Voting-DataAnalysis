#import module
import os
#import module to read csv files
import csv

#declare variables
total_votes = 0
votes_for_Correy = 0
votes_for_Khan = 0
votes_for_Li = 0
votes_for_OTooley = 0

#path to collect data from csv file
election_csv = os.path.join('C:\\Users\\loren\\Desktop\\python-challenge\\PyPoll\\Resources\\election_data.csv')

#open the csv, make sure it is split/read by the correct delimiter: ,
with open (election_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#need to skip header row
    csvheader = next(csvfile)

#loop through the data to find the results we need (rememnber to indent correctly)
    for row in csvreader:
        total_votes = total_votes + 1

#If the name of one of the candidates,which can be found in row 2 (because we are counting from 0), is found then total up the number of votes they got
        if (row[2] == "Correy"):
            votes_for_Correy = votes_for_Correy + 1

        elif (row[2] == "Khan"):
            votes_for_Khan = votes_for_Khan + 1

        elif (row[2] == "Li"):
            votes_for_Li = votes_for_Li + 1

        else:
            votes_for_OTooley = votes_for_OTooley + 1

# calculate the percent of votes for each candidate
percent_of_votes_for_Correy = round((votes_for_Correy/total_votes)*100)

percent_of_votes_for_Khan = round((votes_for_Khan/total_votes)*100)

percent_of_votes_for_Li = round((votes_for_Li/total_votes)*100)

percent_of_votes_for_OTooley = round((votes_for_OTooley/total_votes)*100)


#create a function of the max of votes of each candidate to determine who the winner is. We will then use an if statement to declare the winner
winner = max(votes_for_Correy, votes_for_Khan, votes_for_Li, votes_for_OTooley)
if winner == votes_for_Correy:
    winner = "Correy"
elif winner == votes_for_Khan:
    winner = "Khan"
elif winner == votes_for_Li:
    winner = "Li"
else:
    winner = "O'Tooley"

#Print out the results
print("Election Results")
print("--------------------")
print(f"Total Votes: {total_votes}") 
print("---------------------")
print(f"Khan: {percent_of_votes_for_Khan}% ({votes_for_Khan}) ")
print(f"Correy: {percent_of_votes_for_Correy}% ({votes_for_Correy}) ")
print(f"Li: {percent_of_votes_for_Li}% ({votes_for_Li}) ")
print(f"O'Tooley: {percent_of_votes_for_OTooley}% ({votes_for_OTooley}) ")
print('----------------------')
print(f"Winner: {winner}")
print('----------------------')

#Naming the path of the text file to write the results in
output_file = os.path.join('C:\\Users\\loren\\Desktop\\python-challenge\\PyPoll\\analysis\\results.txt')

#Open the file to write on it and command it to write each result you want. Remember to use \n to move to the next line
with open(output_file, "w") as text:
    
    text.write('Election Results\n')
    text.write('-----------------------\n')
    text.write(f'Total Votes: {total_votes}\n')
    text.write('-----------------------\n')
    text.write(f"Khan: {percent_of_votes_for_Khan}% ({votes_for_Khan})\n ")
    text.write(f"Correy: {percent_of_votes_for_Correy}% ({votes_for_Correy})\n ")
    text.write(f"Li: {percent_of_votes_for_Li}% ({votes_for_Li})\n ")
    text.write(f"O'Tooley: {percent_of_votes_for_OTooley}% ({votes_for_OTooley})\n ")
    text.write('------------------------\n')
    text.write(f"Winner: {winner}\n")
    text.write('------------------------')







