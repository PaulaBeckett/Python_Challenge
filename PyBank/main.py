#import modules needed for challenge
import os
import csv

#create variable to hold csv file
bank_file_csv = os.path.join("Resources","budget_data.csv")

#create variables to hold information
monthly_variance = []
previous_row = 0

#open and read csv
with open(bank_file_csv, "r") as bank_csv:
    bankreader = csv.reader(bank_csv, delimiter=",")
    header = next(bankreader)
    #test for connection to file
    #print(header)

#getting variance between Profit/Losses months
    for row in bankreader:
        
        #action required to deal with first row of data not requiring a calc on it
        #but hold the P/L number for the next rows calc
        if previous_row == 0:
            previous_row = int(row[1])

        #all other rows have calc applied and stored in list
        else:
            monthly_change = int(row[1]) - previous_row
            previous_row = int(row[1])
            monthly_variance.append(monthly_change)

        #test for correct population of monthly variance list
        #print(monthly_variance)