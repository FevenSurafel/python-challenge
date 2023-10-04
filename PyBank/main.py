import csv

csv_file_path = 'PyBank/Resources/budget_data.csv'

total_months = 0
net_total = 0
previous_profit_loss = None
total_changes = 0
greatest_increase = 0
greatest_increase_date = ''
greatest_decrease = 0
greatest_decrease_date = ''

with open(csv_file_path,'r') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)
        for row in csvreader:
            date = row[0]
            profit_loss = int(row[1])

            total_months += 1
            net_total += profit_loss

            if previous_profit_loss is not None:
                change = profit_loss - previous_profit_loss  
                total_changes += change

                if change > greatest_increase:
                    greatest_increase = change
                    greatest_increase_date = date
                elif change < greatest_decrease:
                    greatest_decrease = change
                    greatest_decrease_date = date

            previous_profit_loss = profit_loss

average_change = total_changes / (total_months - 1)

analysis_results = f'''
Financial Analysis
-----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})
Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})
'''

print(analysis_results)

output_file_path = 'financial_analysis.text'
with open(output_file_path, 'w') as output_file:
    output_file.write(analysis_results)

    print(f'Results exported to {output_file_path}')