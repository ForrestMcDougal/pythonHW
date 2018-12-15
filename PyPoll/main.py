import csv
import os

# read in data
filename = os.path.join('raw_data', 'election_data.csv')
with open(filename, newline='') as csvfile:
    csv = csv.reader(csvfile)
    data = [row for row in csv]

# exclude header in record
len_data = len(data) - 1

# initialize values
winner_name = ''
candidates = []
vote_counts = []
winning_percent = 0

# for each vote
for i in range(1, len_data):
    # if candidate has not already recieved votes
    if data[i][2] not in candidates:
        # add the canditate to list of candidates and give them a vote
        candidates.append(data[i][2])
        vote_counts.append(1)
    else:
        # add a vote to the correct candidate
        vote_counts[candidates.index(data[i][2])] += 1

print('Election Results')
print('-------------------------')
print(f'Total Votes: {len_data}')
print('-------------------------')
# for each candidate
for i in range(len(candidates)):
    # find percent of votes
    percent = vote_counts[i] / len_data * 100
    print(f'{candidates[i]}: {percent:.3f}% ({vote_counts[i]})')
    # find the winner by looping through and comparing percents
    if percent > winning_percent:
        winning_percent = percent
        winner_name = candidates[i]
print('-------------------------')
print(f'Winner: {winner_name}')
print('-------------------------')

file_name = os.path.join('assets', 'election_results.txt')

# write out data to file
with open(file_name, 'w') as fout:
    fout.write('Election Results\n')
    fout.write('-------------------------\n')
    fout.write(f'Total Votes: {len_data}\n')
    fout.write('-------------------------\n')
    for i in range(len(candidates)):
        percent = vote_counts[i] / len_data * 100
        fout.write(f'{candidates[i]}: {percent:.3f}% ({vote_counts[i]})\n')
    fout.write('-------------------------\n')
    fout.write(f'Winner: {winner_name}\n')
    fout.write('-------------------------\n')
