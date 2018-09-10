import os
import csv

budget_csv = os.path.join("budget_data.csv")

maximum = ["", 0]
minimum = ["", 9999999999999999999]

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read and skip the header row first
    csv_header = next(csvfile)

    net_amount = 867884
    for counter, row in enumerate(csvreader):
        if counter > 0:
            # read only the first row after header
            break

        first_value = row[1] # store profit/loss of Jan-2010
        prev_profitloss = row[1] # setting the profit/loss amount in the Jan-2010 as 'previous profit/loss' ie. what the profit/loss amount in Feb-2010 is subtracting to find change between Jan-2010 and Feb-2010
    net_amount += int(row[1])
    total_months = 2 #have to start at 2 since we already read the first 2 rows including header

    for row in csvreader:
        # Find totals
        total_months += 1
        net_amount += int(row[1])

        # Find profit/loss change between current month and prevous month
        monthly_change = int(row[1]) - int(prev_profitloss)
        prev_profitloss = int(row[1]) # setting our 'previous profit/loss' to current row's profit/loss value

        # Calculate the greatest increase
        if (monthly_change > maximum[1]):
            maximum[0] = row[0]
            maximum[1] = monthly_change

        # Calculate the greatest decrease
        if (monthly_change < minimum[1]):
            minimum[0] = row[0]
            minimum[1] = monthly_change


    last_value = row[1] #store profit/loss of Feb-2017
    average = round(((int(last_value) - int(first_value))/(int(total_months - 1))), 2) #calculating average change between months over entire period, rounded to 2 decimals


output = (
    "\nFinancial Analysis\n"
    "----------------------------\n"
    "Total Months:" + str(total_months)+ "\n"
    "Total: $" + str(net_amount) + "\n"
    "Average Change: $" + str(average) + "\n"
    "Greatest Increase in Profits: " + str(maximum[0]) + " ($" + str(maximum[1]) + ")\n"
    "Greatest Decrease in Profits: " + str(minimum[0]) + " ($" + str(minimum[1]) + ")\n"
)

# Print output to terminal
print(output)

# Open/create Summary csv file
Summary_csv = os.path.join("Financial_Analysis.txt")

# write to Summary csv file
with open(Summary_csv, "w") as text_file:
    text_file.write(output)
