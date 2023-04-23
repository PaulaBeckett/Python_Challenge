#import modules needed for challenge
import os
import csv

#create variable to hold csv file
bank_file_csv = os.path.join("Resources","budget_data.csv")

#create variables to hold information
monthly_variance = []
previous_row = 0
#add counters to collect total from each column
total_months = 0
total_pl = 0

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
            #add values from first row to counters
            total_months = total_months + 1
            total_pl = total_pl + int(row[1])

        #all other rows have calc applied and stored in list
        else:
            monthly_change = int(row[1]) - previous_row
            previous_row = int(row[1])
            monthly_variance.append(monthly_change)
            #add values to counters
            total_months = total_months + 1
            total_pl = total_pl + int(row[1])

        #test for correct population of monthly variance list
        #print(monthly_variance)

    #print results for total months/p&l
    print(f'Total Months: {total_months}')
    print(f'Total: ${total_pl}')
    #calculate the average variance to 2 decimal places and print
    average_variance = round(sum(monthly_variance)/len(monthly_variance),2)
    print(f'Average Change: ${average_variance}')
        