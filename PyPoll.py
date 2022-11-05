# Data we need to retrieve
# 1. Total votes cast
# 2. All candidates who received votes
# 3. Percentage of votes each candidate won
# 4. Total number of votes each candidate won
# 5. Winner of election based on popular vote


#DIRECT PATH TO FILE
#assign a variable for the file to load and the path.
###file_to_load = 'Resources/election_results.csv'

#Open election results and read the file.
##election_data = open(file_to_load, 'r')
###with open(file_to_load) as election_data:
    
#To do: Perform analysis
###    print(election_data)
#Close the file.
###election_data.close()

#INDIRECT PATH TO FILE

####Add our dependencies
import csv
import os

####Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

#Open election results and read the file.
##with open(file_to_load) as election_data:

    #To do: read and analyze the data here.
 ##   file_reader= csv.reader(election_data)

    #Print each row in the CSV File.
 ##   for row in file_reader:
 ##       print(row)

    #Print the file object
    #print(election_data)


#USING OPEN AND CLOSE FUNCTIONSA TO WRITE TO A FILE

# Create a filename variable to a direct or indirect path to the file.
##file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.
##open(file_to_save, "w")

#Use the open statement to open the file as a text file
##outfile = open(file_to_save,"w")

# Write some data to the file.
##outfile.write("Hello World")

# Close the file
##outfile.close


#USING WITH STATEMENT TO WRITE TO A FILE

# Create a filename variable to a direct or indirect path to the file.
####Assign a variable to load a file from a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

####Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

####Read and print header row
    headers = next(file_reader)
    print(headers)

# Using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:

# Write some data to the file individually
    ##txt_file.write("Arapahoe, ")
    ##txt_file.write("Denver, ")
    ##txt_file.write("Jefferson, ")

# Write some data to the file as a group
    #####txt_file.write("Arapahoe, Denver, Jefferson")

#Write some data to file as a newline escape sequence
    ####txt_file.write("Arapahoe\nDenver\nJefferson")

#Add the title Counties in the election and all the dashes before the sequence
    txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")

# Close the file
txt_file.close