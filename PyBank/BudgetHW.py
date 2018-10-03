# imported modules
import os
import csv
import math

# Declared variables
Profit = []
Delta_Profit = []
total_profit = 0
total_delta = 0.0
Delta = 0.0
Counter = 0
y = 0.0
Average_Profit = 0.0

# Path to collect data from the Resources folder
budgetCSV = os.path.join('C:/Users/Dgrimm/Desktop/PythonStuff/03 -Python\Homework/Instructions/PyBank/Resources/budget_data.csv')

# Read in the CSV file
with open(budgetCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

# moving all profit data into list and finding length (# of variable)
    for row in csvreader:
        Profit.append(row[1])  
    Length = (len(Profit))
# looping through the profit list to find the total
    while (y < (len(Profit)-1)):  
        if Counter < 86:
            total_profit = int(Profit[Counter]) + total_profit
            Counter = Counter + 1
        else:
            break
# looping through the list by the list length to calculate the delta every month and putting it into a list
    while (y < (len(Profit)-1)): 
        if Counter < 86:
            Delta = int(Profit[Counter+1])-int(Profit[Counter])
            Delta_Profit.append(Delta)
            Counter = Counter + 1
        else:
            break
    
    while (y < (len(Profit)-1)):  
        if Counter < 86:
            total_delta = int(Delta_Profit[Counter]) + total_delta
            Counter = Counter + 1
        else:
            break 
   

    #Average_change = (Delta_Profit/(len(Profit)))
    #print(Average_Change)

# print references
print("Financial Analysis")
print("---------------------")
print("$"+str(total_profit))
print("Total Months: " + str(len(Profit)))
#print("Average Change: " + str(Average_change)
print("Average Increase in Profits: " )
print("Average Decrease in Profit: " )
print(str(Delta_Profit))
print(Delta)


