# imported modules
import os
import csv
import math

# Declared variables
Profit = []
Dates = []
Delta_Profit = []
total_profit = 0
total_delta = 0.0
Delta = 0.0
Counter = 0
Counter2 = 0
Counter3 = 0
y = 0.0
Average_Profit = 0.0
High_Date = 0
High_Date_Data = 0
Low_Date = 0
Low_Date_Data = 0

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
        Dates.append(row[0])
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
        if Counter2 < 85:
            Delta = int(Profit[Counter2+1])-int(Profit[Counter2])
            Delta_Profit.append(Delta)
            Counter2 = Counter2 + 1
        else:
            break
    
    while (y < (len(Profit)-1)):  
        if Counter3 < 85:
            total_delta = int(Delta_Profit[Counter3]) + total_delta
            Counter3 = Counter3 + 1
        else:
           break 
 
 # Calculating Dates for highest profit and loweest profit
High_Date = int(Delta_Profit.index((max(Delta_Profit))))
High_Date_Data = (Dates[High_Date+1])
Low_Date = int(Delta_Profit.index((min(Delta_Profit))))
Low_Date_Data = (Dates[Low_Date+1])

# print references
print("Financial Analysis")
print("---------------------")
print("Total: " + "$"+str(total_profit))
print("Total Months: " + str(len(Profit)))
print("Average Change: " + "$" + str(int(total_delta/(Length-1))))
print("Average Increase in Profits: " + str(High_Date_Data) + " " +"$" + str(max(Delta_Profit)))
print("Average Decrease in Profit: " + str(Low_Date_Data) + " " +"$" + str(min(Delta_Profit)))


