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
print(percent_of_votes_for_OTooley)


#print(percent_of_votes_for_Correy)
#we need to make the lists for the candidates and their votes so it is easier to find the winner

    #print(votes_for_OTooley)
