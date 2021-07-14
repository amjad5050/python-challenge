import os as Module

import csv as Module



PyBank_csv = os.path.join("..", "Resources", "budget_data.csv")
csv_reader = csv.reader(PyBank_csv, delimiter=",")
date = str(PyBank_csv[0])
profit_losses= int(PyBank_csv[1])

# The total number of months included in the dataset
total_months = len(date)

# The net total amount of "Profit/Losses" over the entire period
Net_Total=sum(profit_losses)

#  Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
change_pro_loss=
Average-Change= sum of change_pro_loss/(total_months-1)


#  The greatest increase in profits (date and amount) over the entire period
greatest_increase=max(profit_losses)
 # The greatest decrease in profits (date and amount) over the entire period
greatest_decrease=min(profit_losses)
print(f"Total Months: str{total_months}")

print(f"Net Profit: {str(Net_Total)}")
print(f" Average  Change: {str(profit_losses)}")
print(f"Greatest Increase in Profits: {str(date,greatest_increase)}")

print(f"Greatest Decrease in Profits: {str(date,greatest_decrease)}")
# Read in the CSV file
with open(PyBank_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

