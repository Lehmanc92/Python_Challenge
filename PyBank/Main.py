# Import CSV file
import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
print(csvpath)

file_to_output = os.path.join('..', 'Python_Challenge', 'Analysis','Budget_Analysis.csv')

#print(file_to_output)


with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')

    
    # #Read the header row

    csv_header = next(csv_reader)
    print(f'CSV Header: {csv_header}')

    for row in csv_reader:
        print(row)

    for row in csv_file[0]:
        print(row)

