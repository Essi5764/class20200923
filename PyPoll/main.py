import csv
# Importing the election data
candidates = []
candidate_votes = {}
total_vote=0
winning_candidate=""
winning_count=0
with open("election_data.csv", 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    #Find Total vote
    
    # Loop through the data
    for row in csvreader:
        total_vote=total_vote+1
    # If the canditate's name in a row is equal to..., run the 'print_percentages()' function
        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate]=0
        candidate_votes[candidate]=candidate_votes[candidate]+1
    #To find the winner
with open("output.txt","w") as txtfile:

    print(f"-------------------------------------------")
    print(f"Total vote: {total_vote}")
    print(f"-------------------------------------------")
    txtfile.write(f"-------------------------------------------\n")
    txtfile.write(f"Total vote: {total_vote}\n")
    txtfile.write(f"-------------------------------------------\n")
    for candidate in candidate_votes:
        votes=candidate_votes[candidate]
        percent=float(votes)/float(total_vote)*100
        print(f"{candidate}: {percent}% ({votes})")
        txtfile.write(f"{candidate}: {percent}% ({votes})\n")
        if (votes>winning_count):
            winning_count=votes
            winning_candidate=candidate    
        # Print the analysis and export 
        # file as text file with the results
    print(f"-------------------------------------------")
    print(f"Winner: {winning_candidate}")
    print(f"-------------------------------------------")
    txtfile.write(f"-------------------------------------------\n")
    txtfile.write(f"Winner: {winning_candidate}\n")
    txtfile.write(f"-------------------------------------------\n")