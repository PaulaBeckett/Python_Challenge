#import modules needed for challenge
import os
import csv

#create cariable to hold csv file path
election_file_csv = os.path.join("Resources", "election_data.csv")

#create variables to hold information
total_votes = 0
list_candidates = []
vote_candidate = [0,0,0]
#create variable hold percentage of votes
percent_vote = []
#add variable to collect each candidates results
results_list = []

#open and read csv
with open(election_file_csv, "r") as election_csv:
    electionreader = csv.reader(election_csv, delimiter=",")
    header = next(electionreader)
    #test for connection to file
    #print(header)

    for row in electionreader:
        
        #if the candidate name is already in list_candidate
        if str(row[2]) in list_candidates:
            #count the vote
            total_votes = total_votes + 1
            #find which index the candidate is sitting in list_candidate
            vote_choice = str(row[2])
            vote_index = list_candidates.index(vote_choice)
            #add a vote to the vote counter list
            vote_candidate[vote_index] +=1

        #for a new/unique candidate name
        else:
            #add candidate name to list_candidate
            list_candidates.append(str(row[2]))
            #count the vote
            total_votes = total_votes + 1
            #find which index the candidate is sitting in list_candidate
            vote_choice = str(row[2])
            vote_index = list_candidates.index(vote_choice)
            #add a vote to the vote counter list
            vote_candidate[vote_index] +=1
    
    #print total votes
    print(f'Total Votes: {total_votes}')

    #run a loop to update the percentage of votes based on final tallies and total votes
    for candidate in range(3):
        #calc percentage of votes to 3 decimal places
        percent = round(((vote_candidate[candidate])/total_votes)*100,3)
        #add to percentage list
        percent_vote.append(percent)
        #add results to list for each candidate
        results_list.append(f"{list_candidates[candidate]}: {percent_vote[candidate]}% ({vote_candidate[candidate]})")
        #print result list to terminal
        print(f'{results_list[candidate]}')

#test print proper collection of candidates, total votes and number of votes per candidate
#print(total_votes)
#print(list_candidates)
#print(vote_candidate)

#find largest number of votes from tallies
most_votes = max(vote_candidate)
#test print(most_votes)

#using max result find index of this in table
winner_index = vote_candidate.index(max(vote_candidate))
winner = list_candidates[winner_index]
#print winners name to terminal
print(f'Winner: {winner}')

#write results to new text file

#create variable for new file
election_results = os.path.join("Analysis", "Election_Results.txt")

#open new file
with open(election_results, "wt") as txt:
        #define what each line should say
        lines = ["Election Results",
                "---------------------------------------",
                (f'Total Votes: {total_votes}'), 
                "---------------------------------------",
                (f'{results_list[0]}'),
                (f'{results_list[1]}'),
                (f'{results_list[2]}'),
                "---------------------------------------",
                (f'Winner: {winner}')]   
    #loop to write each value in the text file on its own line
        for line in lines:
            txt.write(line)
            txt.write('\n')