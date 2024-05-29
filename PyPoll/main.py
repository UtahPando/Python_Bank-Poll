import os
import csv
Polling_csv = r'Resources\election_data.csv'

# Initialize variables
total_votes = 0
candidate_votes = {}
candidates = []

# Open the CSV file
with open(Polling_csv, newline='', encoding='utf-8') as csvfile:
    # Create a CSV reader object
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row (if there is one)
    next(csvreader)

    # Iterate through each row in the CSV reader object
       # Iterate over each row in the file
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        
        # Count the votes for each candidate
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
            candidates.append(candidate)

# Calculate the percentage of votes each candidate won
percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# Find the winner based on the popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Print the analysis to the terminal
print("Election Results\n")
print("-------------------------\n")
print(f"Total Votes: {total_votes}\n")
print("-------------------------\n")
for candidate in candidates:
    print(f"{candidate}: {percentages[candidate]:.3f}% ({candidate_votes[candidate]})\n")
print("-------------------------\n")
print(f"Winner: {winner}\n")
print("-------------------------\n")

# Export the results to a text file
with open('election_results.md', 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")
    for candidate in candidates:
        output_file.write(f"{candidate}: {percentages[candidate]:.3f}% ({candidate_votes[candidate]})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")

    print(candidates)
    print(candidate_votes)
    print(type(candidate_votes))