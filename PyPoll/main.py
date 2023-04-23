#import modules needed for challenge
import os
import csv

#create cariable to hold csv file path
election_file_csv = os.path.join("Resources", "election_data.csv")

#create variables to hold information
total_votes = 0
list_candidates = []
vote_candidate = [0,0,0]

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

#test print proper collection of candidates, total votes and number of votes per candidate
print(total_votes)
print(list_candidates)
print(vote_candidate)
