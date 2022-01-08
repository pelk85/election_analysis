#Add dependencies
import os
import csv
#Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
##Assign a varibale to save the file to a path 
file_to_save = os.path.join("analysis","election_analysis.txt")

# Initialize a total vote counter. 
total_votes = 0
# Candidate options and candidate votes 
candidate_options = []
candidate_votes = {}
# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


#open the election results and read the file
with open(file_to_load) as election_data: 
     # To Do: Read and Analyze the data 
     file_reader = csv.reader(election_data)
     
     #Read and print the header row 
     headers = next(file_reader)
     
     #print each row in the CSV file
     for row in file_reader:
        
        # Add to the total vote count. 
        total_votes +=1 
        
        # Print the candidate name from each row
        candidate_name = row[2]

        # Add the candidate name to the candidate list
        if candidate_name not in candidate_options:
        
            # add it to the list of candidate options
            candidate_options.append(candidate_name)

            # Begin tracking the candidates vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

# Print the final vote count to the terminal.
    election_results = (       
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    
    print(election_results, end="")
            
    # Save the final vote count to the text file.
    txt_file.write(election_results)


    # Determine the % of votes for each candidate
    # 1. iterate through the candidate list 
    for candidate_name in candidate_votes: 
        # 2. Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # 3. Calculate the % of votes 
        vote_percentage = float(votes) / float(total_votes) * 100
        
        # Determine the winning vote count and candidate 
        # 1. Determine if the votes are greater than the winning count 
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set the winning_count and winning_percent
            winning_count = votes
            winning_percentage = vote_percentage
            # 3. Set the winning_Candidate equal to the candidates name 
            winning_candidate = candidate_name 

        # Set the candidate results variable for printing
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

    winning_candidate_summary = (
        f"-----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-----------------------------\n")
    #  Save the winner results to our text file.
    txt_file.write(winning_candidate_summary)
    print(winning_candidate_summary)
