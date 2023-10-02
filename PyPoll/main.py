import csv

csvpath = "Resources/election_data.csv"

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

percentage_votes = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

winner = max(candidate_votes, key=candidate_votes.get)

output_path = "election_results.txt"
with open(output_path, "w") as file_output:
    results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print (results)
    #file_output.write(results)
    #file.write("-------------------------\n")
    #file.write(f"Total Votes: {total_votes}\n")
    #file.write("-------------------------\n")

    #for candidate, votes in candidate_votes.items():
        #file_output.write(f"{candidate}: {percentage_votes[candidate]:.3f}% ({votes})\n")

    #file_output.write("-------------------------\n")
    #file_output.write(f"Winner: {winner}\n")
    #file_output.write("-------------------------\n")

#print("Analysis exported to", output_path)