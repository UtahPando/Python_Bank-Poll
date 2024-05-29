import os
import csv

Financials_csv = r'Resources\budget_data.csv'

# Lists to store data
Dates = []
P_n_Ls = []
Total_Income = 0

# Open the CSV file
with open(Financials_csv, newline='', encoding='utf-8') as csvfile:
    # Create a CSV reader object
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row (if there is one)
    next(csvreader)
    # Iterate through each row in the CSV reader object
    for row in csvreader:
     # Assuming specific columns for simplicity; adjust indices as necessary
     Date = row[0]
     P_n_L = int(row[1])
     # Append data to lists
     Total_Income += P_n_L 
     Dates.append(Date)
     P_n_Ls.append(P_n_L)

# Initialize variables to store the maximum increase, maximum decrease, and their respective indices
max_increase = 0
max_decrease = 0
cume_difference = 0
increase_index = 0
decrease_index = 0

# Loop through the list of numbers
for i in range(1, len(P_n_Ls)):
    difference = P_n_Ls[i] - P_n_Ls[i-1]
    cume_difference += difference

    # Check for maximum increase
    if difference > max_increase:
        max_increase = difference
        increase_index = i
    
    # Check for maximum decrease
    if difference < max_decrease:
        max_decrease = difference
        decrease_index = i
     
average_value = cume_difference / (len(P_n_Ls)-1)

output_directory = r'analysis' 
output_file = os.path.join(output_directory, "output.md")

# Open the output file for writing
with open(output_file, "w", newline='') as datafile:
#    writer = markdown.writer(datafile)

    # Write the header row
    print("\nFinancial Analysis\n")
    datafile.write("\nFinancial Analysis\n")
    print("-------------------------\n")
    datafile.write("-------------------------\n")
    

    # Write the output rows
    print(f"Total Months: {len(set(Dates))}\n")
    datafile.write(f"Total Months: {len(set(Dates))}\n")
    print(f"Total: ${Total_Income}\n")
    datafile.write(f"Total: ${Total_Income}\n")
    print(f"Average Change: ${round(average_value,2)}\n")
    datafile.write(f"Average Change: ${round(average_value,2)}\n")
    print(f"Greatest Increase in profits: {Dates[increase_index]} (${max_increase})\n")
    datafile.write(f"Greatest Increase in profits: {Dates[increase_index]} (${max_increase})\n")
    print(f"Greatest decrease in profits: {Dates[decrease_index]} (${max_decrease})\n")
    datafile.write(f"Greatest decrease in profits: {Dates[decrease_index]} (${max_decrease})\n")

