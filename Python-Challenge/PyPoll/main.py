#PyPoll script
import os
import csv

total_votes = 0
candidates = [] # Create empty list of candidates
vote_counts = [] # Create empty list of vote counts

electiondata = os.path.join("election_data.csv")
with open (electiondata, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile) #skip header

    for row in csvreader:
        total_votes += 1
        candidate = row[2] # setting the candidate to equal the candidate listed in row[2]

        if candidate in candidates: # if that candidate is found in the candidates list, then...
            index = candidates.index(candidate) # finds index number of first instance candidate is found in list, ex Khan is first in list, so candidates.index is 0
            vote_counts[index] += 1

        else: # otherwise ...
            candidates.append(candidate) # add candidate to list
            vote_counts.append(1) # add 1 to list

    percentages = []
    max_votes = vote_counts[0] # setting the the value at index 0 in vote_counts list as the starting point
    max_index = 0

    for count in range(len(candidates)): # iterating through count in the range (range will be the number of candidates)
        vote_percentage = format(round(vote_counts[count]/total_votes*100), '.3f')
        percentages.append(vote_percentage)
        if vote_counts[count] > max_votes:
            max_votes = vote_counts[count]
            max_index = count
    winner = candidates[max_index]

    # print output to terminal
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {total_votes}")
    for count in range(len(candidates)):
        print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
    print("---------------------------")
    print(f"Winner: {winner}")
    print("---------------------------")

    # create path for new file
    pollingresults = os.path.join("Election Results.txt")

    # write to Summary csv file
    with open(pollingresults, "w") as text_file:
        text_file.write("Election Results\n")
        text_file.write("--------------------------\n")
        text_file.write(f"Total Votes: {total_votes}\n")
        for count in range(len(candidates)):
            text_file.write(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})\n")
        text_file.write("---------------------------\n")
        text_file.write(f"Winner: {winner}\n")
        text_file.write("---------------------------\n")
