#Creating a pathway to our CSV File
import os
import csv
election_data =  os.path.join("election_data.csv")

#Creating our variables for number of candidates, votes, percentage of votes, and number of votes the candidate recieves
candidates=[]
total_votes=0
percent_votes =[]
number_votes=[]

#Opening and reading csvfile, reading the header row
with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

#Adding candidats to our list, and when their name is in our index, adding another vote to their vote count
    for row in csvreader:
        total_votes += 1

        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            number_votes.append(1)
        else:
            index = candidates.index(row[2])
            number_votes[index] += 1

#Creating percentage of votes, rounding 3 places (as shown in the example), adding percentage sign
    for votes in number_votes:
        percentage = (votes/total_votes)*100
        percentage = round(percentage,3)
        percentage = "%.3f%%" % percentage
        
        percent_votes.append(percentage)
        # Testing it worked by using print(percentage)

#Printing the winner
    winner = max(number_votes)
    index = number_votes.index(winner)
    winning_candidate = candidates[index]

#Displaying results
print("Election Results")
print("---------------------")
print(f"Total votes: {str(total_votes)}" )
print("---------------------")
#creating list of candidates
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(number_votes[i])})")
print("---------------------")
print(f"Winner: {winning_candidate}")
print("---------------------")

#Exporting the results to the txt file created through git using touch output.txt
output = open("output.txt","w")
output.write("Election Results\n")
output.write("---------------------\n")
output.write(f"Total votes: {str(total_votes)}\n" )
output.write("---------------------\n")
#creating list of candidates
for i in range(len(candidates)):
    output.write(f"{candidates[i]}: {str(percent_votes[i])} ({str(number_votes[i])})\n")
output.write("---------------------\n")
output.write(f"Winner: {winning_candidate}\n")
output.write("---------------------\n")
