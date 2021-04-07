# Import CSV file
import os
import csv
import statistics as stat

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
# print(csvpath)

# Declaring variables for full csv, header only, and data only

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
# print(data_csv)
# ------------------------------------------------------------------------------------------------------------------------------


def bank_analysis(data):
    
    # Define local variables
    
    months = len(data)
    net_profit_loss = 0
    changes = []
    prev_value = 0
    greatest_increase = 0
    greatest_decrease = 0
    month_increase = ''
    month_decrease = ''
    count = 0


    
    for row in data:

        net_profit_loss += int(row[1])

        

        if row != data[0]:
            
            changes.append(int(row[1]) - prev_value)

            # For each iteration, this will capture the greatest increase and the respective month
            if greatest_increase < changes[count]:
                greatest_increase = changes[count]
                month_increase = row[0]

            # For each iteration, this will capture the greatest decrease and the respective month
            if greatest_decrease > changes[count]:
                greatest_decrease = changes[count]
                month_decrease = row[0]

            #This count increase by one each time the row changes so that the "changes" variable will follow the correct row
            count += 1

        prev_value = int(row[1])

        

        

    avg_change = stat.mean(changes)

#    Final Printout of Financial Analysis in Terminal

    print("Financial Analysis")
    print("----------------------------------------------------------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${net_profit_loss}")
    print(f"Average Change: ${round(avg_change, 2)}")
    print(f"Greatest Increase in Profits: {month_increase} (${str(greatest_increase)})")
    print(f"Greatest Decrease in Profits: {month_decrease} (${str(greatest_decrease)})")
   

#    Creating Final Printout as Output File

    output_path = os.path.join('..', 'Solutions', 'PyBank_Output.txt')
    with open(output_path, 'w', newline='') as txtfile:

        txtfile.writelines(
            
        "Financial Analysis\n"
        "----------------------------------------------------------------------\n"
        f"Total Months: {months}\n"
        f"Total: ${net_profit_loss}\n"
        f"Average Change: ${round(avg_change, 2)}\n"
        f"Greatest Increase in Profits: {month_increase} (${str(greatest_increase)})\n"
        f"Greatest Decrease in Profits: {month_decrease} (${str(greatest_decrease)})\n"




        )
       
    return None

bank_analysis(data_csv)

