# Import os and csv modules
import csv
import os

#Define file paths
csvpath = os.path.join('Resources', 'election_data.csv')
output_file_path = os.path.join('Analysis', 'output.csv')

#Define initial variables
total_votes = 0
candidate_votes = {}
candidates = []

#Open csv file
with open(csvpath) as csvfile:
    
    #Create csv reader object
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Skip headers
    next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        
        # Increment the total number of votes
        total_votes += 1
        
        # Get the candidate name from the current row
        candidate = row[2]
        
        # Check if the candidate is not already in the dictionary
        if candidate not in candidate_votes:
            # Initialize the vote count for the candidate
            candidate_votes[candidate] = 0
            # Add the candidate to the list of candidates
            candidates.append(candidate)
        # Increment the vote count for the candidate
        candidate_votes[candidate] += 1

# Calculate the percentage of votes each candidate won
percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# Find the winner of the election based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Print the analysis results
print("Election Results")
print('-' * 40)
print(f"Total Votes: {total_votes}")
print('-' * 40)
for candidate in candidates:
    print(f"{candidate}: {percentages[candidate]:.3f}% ({candidate_votes[candidate]})")
print('-' * 40)
print(f"Winner: {winner}")
print('-' * 40)

#Prepare the results to appear in text file
result_text = f"Election Results\n"
result_text += f"------------------\n"
result_text += f"Total Votes: {total_votes}\n"
result_text += f"------------------\n"
for candidate in candidates:
    result_text += f"{candidate}: {percentages[candidate]:.3f}% ({candidate_votes[candidate]})\n"
result_text += f"------------------\n"
result_text += f"Winner: {winner}\n"
result_text += f"------------------\n"

# Write results into a txt file
with open(output_file_path, 'w') as file:
    file.write(result_text)