import csv
total_months = 0
net_total = 0
previous_profit_loss = None
total_changes = 0
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""

with open('python-challenge/PyBank/Resources/budget_data.csv','r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        
        for row in csv_reader:
            total_months += 1
            net_total += int(row[1])

            if previous_profit_loss is not None:
                change = int(row[1]) - previous_profit_loss
                total_changes += change

                if change > greatest_increase:
                    greatest_increase = change
                    greatest_increase_date = row [0]
                elif change < greatest_decrease:
                    greatest_decrease = change
                    greatest_decrease_date = row[0]

            previous_profit_loss = int (row[1])

average_change = total_changes / (total_months - 1)

print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} ${greatest_decrease}")