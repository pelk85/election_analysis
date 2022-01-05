#Add dependencies
import os
import csv
#Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
##Assign a varibale to save the file to a path 
file_to_save = os.path.join("analysis","election_analysis.txt")

#open the election results and read the file
with open(file_to_load) as election_data: 
     # To Do: Read and Analyze the data 
     file_reader = csv.reader(election_data)
     headers = next(file_reader)
     print(headers)



# the data we need to retrieve.
# 1. the total number of votes cast
# 2. a complete list of the candidates who recieved votes
# 3. the % of votes each candidate won 
# 4. the total number of votes each candidate won 
# 5. the winner of the election based on pop vote 





# # Assign a variable for the file to load and the path 
# file_to_load = 'Resources/election_results.csv'
# # Open the election results and read the file. 
# with open(file_to_load) as election_data:
#     # To Do: Perform the analysis
#     print(election_data)
# file_to_save = os.path.join("analysis","election_analysis.txt")
# with open(file_to_save, "w") as txt_file: 
#     txt_file.write("Counties in the election\n---------------------\nArapahoe\nDenver\nJefferson")
