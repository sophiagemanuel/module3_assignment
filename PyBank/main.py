# Importing modules and creating a path to the csv file
import os 
import csv
budget_data = os.path.join(os.getcwd(), "budget_data.csv")

#creating our variables
total_months = 0
total_net = 0
value = 0
average_change = 0 

dates = []
profits = []

#opening and reading csv file
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Reading the header row
    csv_header = next(csvreader)

    #Reading first row
    first_row = next(csvreader)
    total_months += 1
    total_net += int(first_row[1])
    value = int(first_row[1])

    #Going through the data starting after the header/first row
    for row in csvreader:
        dates.append(row[0])
        #Calculating the changes and adding it to the list
        change = int(row[1]) - value
        profits.append(change)
        value = int(row[1])
        #Calculating total months and net amount of the profit and losses over the entire period
        total_months += 1
        total_net = total_net + int(row[1])

    #Calculating the greatest increase (marked greatest) and decrease (marked worse) in profits and the average change
    greatest_inc = max(profits)
    greatest_dec = min(profits)
    greatest_index = profits.index(greatest_inc)
    greatest_date = dates[greatest_index]
    worst_index = profits.index(greatest_dec)
    worst_date = dates[worst_index]

    average_change = sum(profits)/len(profits)

#Printing the information out
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_net)}")
print(f"Average Change: ${str(round(average_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_inc)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_dec)})")
