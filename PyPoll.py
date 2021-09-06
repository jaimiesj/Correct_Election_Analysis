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

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)
    headers = next(file_reader)
    print(headers)