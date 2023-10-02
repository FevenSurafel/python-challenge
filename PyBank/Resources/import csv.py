import csv
total_months = 0
net_total = 0
previous_profit_loss = None
total_changes = 0
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""

with open ('budget_data.csv','r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        
        for row in csv_reader:
            total_months += 1
            net_total += int(row[1])

            if previous_profit_loss is not None:
                change = int(row[1]) - previous_profit_loss
                total_changes += change

                if change > greates_increase:
                    greatest_increase = change
                    greatest_increase_date = row [0]
                    