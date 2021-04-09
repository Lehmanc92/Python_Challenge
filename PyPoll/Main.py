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

# Create candidate list by finding all unique candidates in data

for row in data_csv:

    if row[2] not in candidate_list:
        candidate_list.append(row[2])
        candidate_totals[row[2]] = 0
        candidate_votes.append(1)
    
    #Tally votes for each candidate
    
    else:
        candidate_votes[candidate_list.index(row[2])] += 1

# for candidate in candidate_list:
#     candidate_totals[candidate] = 0

# for row in data_csv:
#     if 


print(candidate_list)
print(candidate_votes)
print(candidate_totals)