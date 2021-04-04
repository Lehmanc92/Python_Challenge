# Import CSV file
import os
import csv
import statistics as stat

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
# print(csvpath)

file_to_output = os.path.join('..', 'Python_Challenge', 'Analysis','Budget_Analysis.csv')

#print(file_to_output)

full_csv = []
header_csv = []
data_csv = []


with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')

    # print(csv_reader)

    # #Read the header row

    csv_header = next(csv_reader)
    # print(f'CSV Header: {csv_header}')

    header_csv.append(csv_header)

    for row in csv_reader:
        data_csv.append(row)

# print(header_csv)

# for row in data_csv:
#     print(row[1])

# ------------------------------------------------------------------------------------------------------------------------------


def bank_analysis(data):
    
    # Define local variables
    
    months = len(data)
    net_profit_loss = 0
    changes = []
    prev_value = 0
    
    for row in data:

        net_profit_loss += int(row[1])

        

        if row != data[0]:
            
            changes.append(int(row[1]) - prev_value)

        prev_value = int(row[1])

    avg_change = stat.mean(changes)

    print(months)
    #print(changes)
    print(round(avg_change, 2))

    return net_profit_loss

print(bank_analysis(data_csv))

