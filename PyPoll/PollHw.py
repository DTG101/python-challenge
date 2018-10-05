# imported modules
import os
import csv
import numpy as np

# Declared variables
Poll = []
Li = 0
Khan = 0
OTooley = 0
Correy = 0

# Path to collect data from the Resources folder
pollCSV = os.path.join(r"C:\Users\Dgrimm\Desktop\PythonStuff\03 -Python\Homework\Instructions\PyPoll\Resources\election_data.csv")

# Read in the CSV file
with open(pollCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

# moving all poll data into list and finding length (# of variable)
    for row in csvreader:
        Poll.append(row[2])  
    Length = (len(Poll))

# Vote counting
for row in Poll:  
    if row == "Khan":
        Khan = 1 + Khan
    elif row == "Correy":
        Correy = 1 + Correy
    elif row == "Li":
        Li = 1 + Li
    elif row == "O'Tooley":
        OTooley = 1 + OTooley
# Calculating winner
    if Khan > Li and Khan > OTooley and Khan > Correy:
        Winner = "Khan"
    elif Li > Khan and Li > OTooley and Li > Correy:
        Winner = "Li"
    elif OTooley > Khan and OTooley > Li and OTooley > Correy:
        Winner = "OTooley"
    elif Correy > Khan and Correy > OTooley and Correy > Li:
        Winner = "Correy"


# Print references
print("Election Results")
print("-----------------")
print("Total Votes: " + str(Length))
print("-----------------")
print("Khan: " + str(Khan) + " " + "{0:.0%}".format(Khan/Length))
print("Correy: " + str(Correy) + " " + "{0:.0%}".format(Correy/Length))
print("Li: " + str(Li) + " " + "{0:.0%}".format(Li/Length))
print("O'Tooley: " + str(OTooley) + " " + "{0:.0%}".format(OTooley/Length))
print("-----------------")
print("Winner: " + str(Winner))   
print("-----------------")

