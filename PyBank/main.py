import csv
import os

# read in budget data
filename = os.path.join('raw_data', 'budget_data.csv')
with open(filename, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    data = [row for row in csvreader]

# Exclude header for record
len_data = len(data) - 1

# initialize values
total_profit = 0
avg_change = 0
increase_amount = 0
increase_date = ''
decrease_amount = 0
decrease_date = ''

# find months with the greatest increase and decrease in profit
for i in range(1, len(data)):
    total_profit += int(data[i][1])
    if int(data[i][1]) > increase_amount:
        increase_amount = int(data[i][1])
        increase_date = data[i][0]
    elif int(data[i][1]) < decrease_amount:
        decrease_amount = int(data[i][1])
        decrease_date = data[i][0]

# store month to month change in list
change = [int(data[i][1]) - int(data[i-1][1]) for i in range(2, len(data))]

# find average change from month to month using list built-ins
avg_change = sum(change) / len(change)

print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {len_data}')
print(f'Total: ${total_profit}')
print(f'Average Change: ${avg_change:.2f}')
print(f'Greatest Increse in Profits: {increase_date} (${increase_amount})')
print(f'Greatest Decrease in Profits: {decrease_date} (${decrease_amount})')

# Write out text file with information
filename = os.path.join('assets', 'financial_analysis.txt')
with open(filename, 'w') as fout:
    fout.write('Financial Analysis\n')
    fout.write('----------------------------\n')
    fout.write(f'Total Months: {len_data}\n')
    fout.write(f'Total: ${total_profit}\n')
    fout.write(f'Average Change: ${avg_change:.2f}\n')
    fout.write(f'Greatest Increase in Profits: {increase_date} (${increase_amount})\n')
    fout.write(f'Greatest Decrease in Profits: {decrease_date} (${decrease_amount})\n')
