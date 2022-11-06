#Add our dependencies
import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to load a file from a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Add vote counter
total_votes = 0

#1a. Declare new list for candidate options
candidate_options = [ ]

#1b. Declare empty dictionary
candidate_votes = { }

#4a. Winning Candidate and Winning Count Tracker

winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

#Read the header row
    headers = next(file_reader)

#Print each row in the CSV File.
    for row in file_reader:
#        print(row) 
        total_votes += 1
# Print the candidate name from each row
        candidate_name = row [2]

# Add Name to list
        #candidate_options.append(candidate_name)

#Unique candidate names
        if candidate_name not in candidate_options:
#If not in current list, add to it          
            candidate_options.append(candidate_name)
# Track candidate vote count starting from 0
            candidate_votes[candidate_name] = 0
#Add a vote to that candidate each time the candidates name appears            
        candidate_votes[candidate_name] += 1
#Save results to txt file
with open(file_to_save, "w") as txt_file:

# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
#Writing results to file
    txt_file.write(election_results)

#3. Print out total votes
#        print(total_votes)

#Print out candidate list
#    print(candidate_options)

#percentage of total votes for each candidate
#(candidate vote count / total votes) * 100 = that candidates percentage
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
# votes to the terminal.
## - Per 3.6.1 commenting out line below
###     print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
# Determine winning vote count and candidate
# 4aa. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
# 4ab. If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
     # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
     
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

## - Per 3.6.1 commenting out line below
###print(winning_candidate_summary)

#Print each candidate and % votes with f format
#print(f"{candidate_name}: received {vote_percentage}% of the vote.")

#Print Candidate Votes
#print(candidate_votes)
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)