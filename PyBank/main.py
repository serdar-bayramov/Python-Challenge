import csv
import os

budget_csv = os.path.join('.', 'Resources', 'budget_data.csv')



""""create main function for data analysis"""
def budget_analysis(budget):

    year = str(budget[0])
    for row in csvreader:
        if int(row[1]) > 0:
            row[1] = profit
            profit = float(budget[1])
        else:
            row[1] = loss
            loss = float(budget[1])

        for j in row[1]:
                change = row[j+1] - row[j]
                avg_change = sum(change)/len(change)
                increase_profit = max(change)
                if row[1] == increase_profit:
                    increase_month = row[0]
                decrease_profit = min(change)
                if row[1] == decrease_profit:
                    decrease_month = row[0]

    total_months = [sum(row[0]) for row in csvreader]
    #total_months = str(budget[0]).count()
    total_profit = [sum(row[1] for row in csvreader)]
    #total_profit = sum(budget[1])

    print("Financial Analysis")
    print("................................")
    print("Average Change: " + "$" + avg_change)
    print("Greatest Increase In Profits: " + increase_month + "("+increase_profit+")")
    print("Greatest Decrease In Profits: " + decrease_month + "("+decrease_profit+")")

with open(budget_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    for row in csvreader:
        budget_analysis(row)


