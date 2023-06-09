#import modules needed for challenge
import os
import csv

#create variable to hold csv file path
bank_file_csv = os.path.join("Resources","budget_data.csv")

#create variables to hold information
monthly_variance = []
previous_row = 0
#add counters to collect total from each column
total_months = 0
total_pl = 0
#add variable to store date
date = []

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
            #add row date to list
            date.append(str(row[0]))

        #all other rows have calc applied and stored in list
        else:
            monthly_change = int(row[1]) - previous_row
            previous_row = int(row[1])
            monthly_variance.append(monthly_change)
            #add values to counters
            total_months = total_months + 1
            total_pl = total_pl + int(row[1])
            #add row date to list
            date.append(str(row[0]))

        #test for correct population of monthly variance list
        #print(monthly_variance)

#print results for total months/p&l
print(f'Total Months: {total_months}')
print(f'Total: ${total_pl}')

#calculate the average variance to 2 decimal places and print
average_variance = round(sum(monthly_variance)/len(monthly_variance),2)
print(f'Average Change: ${average_variance}')

#calc and store max increase
greatest_increase = max(monthly_variance)
#to find relative month. Add 1 as monthly variance list did not include the first row of data
max_inc = monthly_variance.index(max(monthly_variance)) + 1
#test print for correct list index
#print(max_inc)
#date of max increase  
inc_date = date[max_inc]
#test print for correct date returned
#print(inc_date)

#repeat above calc for biggest decrease
greatest_decrease = min(monthly_variance)
max_dec = monthly_variance.index(min(monthly_variance)) + 1
#test print(max_dec)
dec_date = date[max_dec]
#test print(dec_date)

#display min/max profits
print(f'Greatest Increase in Profits: {inc_date} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {dec_date} (${greatest_decrease})')

#write results to a new text file

#variable for new text file path
bank_results = os.path.join("Analysis", "Financial_Analysis.txt")

#open new file
with open(bank_results,"wt") as txt:
#define what each line should say, in a list
    lines = ["Financial Analysis",
            "---------------------------------------------",
            (f'Total Months: {total_months}'),
            (f'Total: ${total_pl}'),
            (f'Average Change: ${average_variance}'),
            (f'Greatest Increase in Profits: {inc_date} (${greatest_increase})'),
            (f'Greatest Decrease in Profits: {dec_date} (${greatest_decrease})')]
    #loop to write each value in the text file on it's own line
    for line in lines:
        txt.write(line)
        txt.write('\n')

