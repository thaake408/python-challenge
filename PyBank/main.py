# Import os and csv dependencies
import os
import csv

# Establish csv file path
csvpath = os.path.join("..","PyBank", "Resources","budget_data.csv")

# Make empty lists to iterate through rows for the total number of months, total amount of profit, and profit changes in the dataset

total_months = []

total_profit = []

profit_changes = []

# Open and read csv file
with open(csvpath) as csvfile:
    
    # Define csvreader variable
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip header row (row 0) to iterate values starting in row 1 and so on
    header = next(csvreader)
    
    # Iterate through the rows of data stored in csvreader variable
    for row in csvreader:
        
        # Append total months and total profits to the correct lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))

# Iterate through the Profit/Losses column to obtain monthly profit_changes       
# Subtracting 1 from the length is a common practice when iterating over indices because Python uses zero-based indexing. This ensures that the loop doesn't go out of bounds.
for x in range(len(total_profit) - 1):
                            
        # Append the difference between two months to profit_changes
        profit_changes.append(total_profit[x+1] - total_profit[x])
                            
# Calculate the max/min values of profit_changes list
greatest_increase_number = max(profit_changes)
greatest_decrease_number = min(profit_changes)

# Determine the max/min values that correspond to the appropriate month using the max/min values from the profit_changes list
# Add 1 at the end of this formula since the month associated with change is the next month or + 1 month
greatest_increase_month = profit_changes.index(max(profit_changes)) + 1
greatest_decrease_month = profit_changes.index(min(profit_changes)) + 1 
                            
# Print Statements 
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period

print("PyBank Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(profit_changes)/len(profit_changes),2)}")
print(f"Greatest Increase in Profits: {total_months[greatest_increase_month]} (${(str(greatest_increase_number))})")
print(f"Greatest Decrease in Profits: {total_months[greatest_decrease_month]} (${(str(greatest_decrease_number))})")

# Establish csv_output_path path to create new txt file
csv_output_path = os.path.join("analysis","PyBank_Financial_Analysis_Results.txt")
                            
# Use "w" in this formula to "write" the file
with open(csv_output_path,"w") as file:
    
    # Print Financial_Analysis_Summary 
    file.write("PyBank Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(profit_changes)/len(profit_changes),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[greatest_increase_month]} (${(str(greatest_increase_number))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[greatest_decrease_month]} (${(str(greatest_decrease_number))})")


    