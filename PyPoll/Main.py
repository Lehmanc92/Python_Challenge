# Import CSV file
import os
import csv
import statistics as stat

csvpath = os.path.join('..', 'Resources', 'election_data.csv')
# print(csvpath)

# Declaring variables for full csv, header only, and data only
full_csv = []
header_csv = []
data_csv = []


with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')

    print(csv_reader)

    # #Read the header row

    csv_header = next(csv_reader)
    


    header_csv.append(csv_header) #Prints headers to global variable

    for row in csv_reader:  #Prints all data in CSV to global variable
        data_csv.append(row)

# ----------------------------------------------------------------------------------------

# Declaring variables

total_votes = 0
candidate_list = []
candidate_votes = []
candidate_totals = {}
candidate_percentages = []
winning_vote = 0
winner = ""

#  This for-loop will find all unique candidates and tally up all of their votes

for row in data_csv:

    # This if statement sets up a candidate if they have not been encountered in the file yet
    if row[2] not in candidate_list:
        candidate_list.append(row[2])  #This finds any unique candidate name and adds it to candidate_list
        candidate_totals[row[2]] = 0   #This creates a dictionary with the unique candidate as a key and their first vote as the value
        candidate_votes.append(1)     #This updates the vote count for each candidate in a separate candidate_votes list
        total_votes += 1              #Updates the total vote count
    
    #Tally votes for each candidate if they're already in the list
    
    else:
        candidate_votes[candidate_list.index(row[2])] += 1 #Updates the individual's vote count in the candidate_votes list
        total_votes += 1            #Updates the total vote count

# calculates the percentages for each candidate and appends them to the candidate_percentages list
for vote in candidate_votes:
    candidate_percentages.append(round((vote / total_votes) * 100, 3))

for vote in range(len(candidate_votes)):
    if candidate_votes[vote] >= winning_vote:
        winner = candidate_list[vote]
        winning_vote = candidate_votes[vote]

candidate_summary = ''
for candidate in range(len(candidate_list)):
       candidate_summary += candidate_list[candidate] + ": " + str(candidate_percentages[candidate]) + "% (" + str(candidate_votes[candidate]) + ")\n"

print(candidate_summary)
# print(candidate_list)
# print(candidate_votes)
# print(candidate_totals)
# print(candidate_percentages)
# print(total_votes)
# print(winner)
# print(winning_vote)

print(
    f'Election Results\n'
    f'-------------------------------------------------------\n'
    f'Total Votes: {total_votes}\n'
    f'-------------------------------------------------------\n'
    f'{candidate_summary}'
    f'-------------------------------------------------------\n'
    f'Winner: {winner}\n'
    f'-------------------------------------------------------\n')


#    Creating Final Printout as Output File

output_path = os.path.join('..', 'Solutions', 'PyPoll_Output.txt')
with open(output_path, 'w', newline='') as txtfile:

    txtfile.writelines(
        
    f'Election Results\n'
    f'-------------------------------------------------------\n'
    f'Total Votes: {total_votes}\n'
    f'-------------------------------------------------------\n'
    f'{candidate_summary}'
    f'-------------------------------------------------------\n'
    f'Winner: {winner}\n'
    f'-------------------------------------------------------\n'




        )
    
