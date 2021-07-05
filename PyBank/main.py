import os
import csv


budget_csv = os.path.join('.', 'Resources', 'budget_data.csv')
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    month_counter = 0
    total = 0
    month_list = []
    profit = []
    dict={}
    for row in csvreader:
        
        month_counter = month_counter + 1
        total += int(row[1])
        month_list.append(row[0])
        profit.append(row[1])

    difference = [int(y) - int(x) for x, y in zip(profit, profit[1:])]
    avg_difference = round(sum(difference)/len(difference), 2)
    

    print("Financial Analysis")
    print("---------------------------")
    print("Total months: " + str(month_counter))
    print("Total: " + str(total))
    print("Average Change: " + "$" + str(avg_difference))
    
    #print("Greatest Increase In Profits: " + increase_month + "("+increase_profit+")")
    #print("Greatest Decrease In Profits: " + decrease_month + "("+decrease_profit+")")