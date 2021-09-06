# # The data we need to retrieve.
# import csv
# import os
# # 1. The total number of votes cast
# # 2. A complete list of candiates who received votes
# # 3. The percentage of votes each candidate won
# # 4. The total number of votes each candidate won
# # 5. The winner of the election based on popular vote
# # Assign a variable for the file to load and the path.
# # file_to_load = os.path.join("Resources", "election_results.csv")
# # # Open the election results and read the file.
# # #using open() function
# # #election_data = open(file_to_load, 'r')
# # with open(file_to_load) as election_data:
# #     # To do: perform analysis
# #     print(election_data)
# # Close the file
# #using close() function
# #election_data.close()
# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Using the with statement open the file as a text file.
# #using open function
# #outfile = open(file_to_save, "w")
# with open(file_to_save, "w") as txt_file:
# # Write some data to the file.
# #outfile.write("Hello World")
#     txt_file.write("Counties in the Election\n--------------------\nArapahoe\nDenver\nJefferson")

# # Close the file
# #using close function
# #outfile.close()

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#add the total vote counter before with open() statement so it will reset with each loop
total_votes = 0

# declare a new list/candidate options
candidate_options = []

#declare dictionary
candidate_votes = {}

#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)
    print(headers)

    #Print each row in the CSV file.
    for row in file_reader:
        print(row)
        # Add to the total vote count
        total_votes += 1
        #print candidate name for each row
        candidate_name = row[2]
        
        #If candidate not on list
        if candidate_name not in candidate_options:

            #add the candidate name to the candidate llist
            candidate_options.append(candidate_name)

            #track candidate vote count
            candidate_votes[candidate_name] = 0

        #add a vote to candidate count
        candidate_votes[candidate_name] += 1

# determine percentage of votes by looping through
#iterate through the candidate list
for candidate_name in candidate_votes:
    #retrieve vote count of candidate
    votes = candidate_votes[candidate_name]
    #calculate percentage
    vote_percentage = float(votes)/float(total_votes) * 100
    #print the candidate name and percentage of votes
    #print(f"{candidate_name} received {vote_percentage:.1f}% of the vote")

    #to do: print out each candidate's name, vote count, and percentage of votes to the terminal
    print(f"{candidate_name} {vote_percentage:.1f}% ({votes:,})\n")

    #determine winning vot count and candidate
    #determine if the votes is greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #if true then set winning_count = votes and winning_percent = #vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # and set the winning candidate equal to candidate's name
        winning_candidate = candidate_name

#to do: print out the winning candidate, vote count and percentage to terminal    
winning_candidate_summary = (
    f"---------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"---------------------------------\n")
print(winning_candidate_summary)

#Print the total votes
# print(total_votes)
# print(candidate_options)
# print(candidate_votes)

