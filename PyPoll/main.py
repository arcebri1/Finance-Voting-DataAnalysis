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

#declare variables
total_votes = 0
votes_for_Correy = 0
votes_for_Khan = 0
votes_for_Li = 0
votes_for_OTooley = 0

#path to collect data from excel file
election_csv = os.path.join('C:\\Users\\loren\\Desktop\\python-challenge\\PyPoll\\Resources\\election_data.csv')

#open the csv
with open (election_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(reader)

#skip header row first
    csvheader = next(csvfile)
    #print(f'csv header: {csvheader}')

#read each row after the header
    for row in csvreader:
        total_votes = total_votes + 1
        #print(total_votes)

#If the name of one of the candidates within row 2 (because we are counting from 0) is found then add them up
        if (row[2] == "Correy"):
            votes_for_Correy = votes_for_Correy + 1

        elif (row[2] == "Khan"):
            votes_for_Khan = votes_for_Khan + 1

        elif (row[2] == "Li"):
            votes_for_Li = votes_for_Li + 1

        else: #row[2] == "O'Tooley":
            votes_for_OTooley = votes_for_OTooley + 1

# calculate the percent of votes for each candidate
percent_of_votes_for_Correy = round((votes_for_Correy/total_votes)*100)
#print(percent_of_votes_for_Correy)
percent_of_votes_for_Khan = round((votes_for_Khan/total_votes)*100)
#print(percent_of_votes_for_Khan)
percent_of_votes_for_Li = round((votes_for_Li/total_votes)*100)
#print(percent_of_votes_for_Li)
percent_of_votes_for_OTooley = round((votes_for_OTooley/total_votes)*100)
#print(percent_of_votes_for_OTooley)

#create a function of the max of votes of each candidate to obtain the winner. We will then use an if statement to declare the winner
winner = max(votes_for_Correy, votes_for_Khan, votes_for_Li, votes_for_OTooley)
if winner == votes_for_Correy:
    winner = "Correy"
elif winner == votes_for_Khan:
    winner = "Khan"
elif winner == votes_for_Li:
    winner = "Li"
else:
    winner = "O'Tooley"
#print(winner)

#print("Election Results")
#print("--------------------")
#print(f"Total Votes: {total_votes}") 
#print("---------------------")
#print(f"Khan: {percent_of_votes_for_Khan}% ({votes_for_Khan}) ")
#print(f"Correy: {percent_of_votes_for_Correy}% ({votes_for_Correy}) ")
#print(f"Li: {percent_of_votes_for_Li}% ({votes_for_Li}) ")
#print(f"O'Tooley: {percent_of_votes_for_OTooley}% ({votes_for_OTooley}) ")
#print('----------------------')
#print(f"Winner: {winner}")
#print('----------------------')

output_file = os.path.join('C:\\Users\\loren\\Desktop\\python-challenge\\PyPoll\\analysis\\results.txt')
with open(output_file, "w") as text:
    #text.write('testing')
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







