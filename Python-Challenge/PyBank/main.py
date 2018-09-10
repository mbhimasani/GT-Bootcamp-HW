import os
import csv

budget_csv = os.path.join("budget_data.csv")


with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read and skip the header row first
    csv_header = next(csvfile)
    print(f"Header: {csv_header}") #print Header





    for counter, row in enumerate(csvreader):
        if counter > 0:
            #read only the first row after header
            break
        first_value = row[1] #print first row, second column


    total_months = 2
    net_amount = 0
    for row in csvreader:
        total_months = total_months + 1
        net_amount += int(row[1])
    print("Total Months:" + str(total_months))
    print("Total: $" + str(net_amount))
    last_value = row[1]

    average = round(((int(last_value) - int(first_value))/(int(total_months - 1))), 2)
    print("Average Change: $" + str(average))
