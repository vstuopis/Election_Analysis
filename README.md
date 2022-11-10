# Election Analysis

## Election Audit
### Overview
The election audit analysis was conducted to provide election results to the election commission. We focused on understanding and providing the election data both by county and by individual candidate to the commission. 

### Results
- There were a total of 369,711 votes cast in this congressional election
- Denver County had the largest number of votes
- Diana DeGette won the election with 272,892 votes (73.8% of the vote)
- [County and Individual Candidate Voting Results Breakdown](analysis/election_results.txt)
### Summary
With the script provided, this will only allow for the election commission to use this going forward in addition to making any necessary changes as time goes on for future updates. One example of a modification that can be made to the script is if we need to tabulate results from different counties where their data is in a cvs file. In this case, the only update required for the script would be me update the file_to_load path in line 9. Another change which can be made to the script is if we wanted to put the number of votes first with the total percentage in the parentheses. This would require some modifications to the script on line 104 when printing the county results to the terminal, we would need to swap the order of county_percentage and county_vote_count in the f string.

## Software Used
- Python 3.7 (64-bit)
- Visual Studio Code 1.73.0
