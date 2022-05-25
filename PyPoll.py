<<<<<<< HEAD
# Add our dependencies

import csv
import os

# Assign a variable to load a file from a path

file_to_load = "Resources/election_results.csv"

# Assign a variable to save the file to a path

file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter

total_votes = 0

# Candidate Options

candidate_options = []

candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row

    headers = next(file_reader)

    # Print each row in the CSV file
    
    for row in file_reader:

# Add to the total vote count

        total_votes += 1

# Print the candidate name from each row

        candidate_name = row[2]

# Add the candidate name to the candidate list

        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

print(total_votes)

print(candidate_options)

print(candidate_votes)

# Print percentage of votes each candidate received
for candidate_name in candidate_votes:

    votes = candidate_votes[candidate_name]

    vote_percentage = float(votes) / float(total_votes) * 100

    print(f"{candidate_name}: received {round(vote_percentage,1)}% of the vote.")

    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    if (votes > winning_count) and (vote_percentage > winning_percentage):
     # 2. If true then set winning_count = votes and winning_percent =
     # vote_percentage.
     winning_count = votes
     winning_percentage = vote_percentage
     # 3. Set the winning_candidate equal to the candidate's name.
     winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
=======
import csv
import os

file_to_load = "Resources/election_results.csv"

file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)
>>>>>>> cc4ae00b9935b5c74939fa29f4f9a070a28e6893
