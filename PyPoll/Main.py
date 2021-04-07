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
candidate_totals = {}

# Create candidate list

for row in data_csv:
    if row[2] not in candidate_list:
        candidate_list.append(row[2])

# for candidate in candidate_list:
#     candidate_totals.update(candidate)


print(candidate_list)
print(candidate_totals)