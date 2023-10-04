import csv

csvpath = "PyPoll/Resources/election_data.csv"

total_votes = 0
candidate_votes = {}

with open(csvpath, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)
    
    for row in csv_reader:
        total_votes += 1
        candidate = row[2]

        if candidate in candidate_votes:
            candidate_votes[candidate] +=1
        else:
            candidate_votes[candidate] = 1

percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

winner = max(candidate_votes, key=candidate_votes.get)

print("Election Results")
print("-------------------------")
print(f"Total Votes:, {total_votes}")
print("-------------------------")

for candidate, votes in candidate_votes.items():
    #percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentages}% ({votes})")

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

output_file =  "election_results.txt"
with open(output_file, "w") as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")

    for candidate, votes in candidate_votes.items():
        file.write(f"{candidate}: {percentages[candidate]:.3f}% ({votes})\n")

    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")