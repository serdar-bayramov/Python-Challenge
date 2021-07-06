import os
import csv

"""add path for budget_data.csv file"""
budget_csv = os.path.join('.', 'Resources', 'budget_data.csv')

"""open csv.file in read mode"""

with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

"""add/set counters to 0 and add empty lists to hold values"""

    month_counter = 0
    total = 0
    month_list = []
    profit = []

"""create for loop to loop through rows in csvreader"""

    for row in csvreader:
        
        month_counter = month_counter + 1
        total += int(row[1])
        
    """append lists with months and profit/loss from csv.file"""

        month_list.append(row[0])
        profit.append(row[1])

"""calculate the difference between profits/losses for each month and get the average"""

    difference = [int(y) - int(x) for x, y in zip(profit, profit[1:])]
    avg_difference = round(sum(difference)/len(difference), 2)
    
    """find max profit, get the index and extract the month from months storing list"""

    for month, max_profit in zip(month_list,profit):
        max_profit = max(difference)
        index_max = difference.index(max_profit)
        MaxProfitMonth = month_list[index_max+1]

    """find min profit, get the index and extract the month from months storing list"""

    for month, min_profit in zip(month_list,profit):
        min_profit = min(difference)
        index_min = difference.index(min_profit)
        MinProfitMonth = month_list[index_min+1]

"""assign variables for output to be printed"""

    TitleResult = "Financial Analysis \n--------------------------"
    TotalMonthResult = "\n Total months: " + str(month_counter)
    TotalResult = "\n Total: " + str(total)
    AvgChangeResult = "\n Average Change: " + "$" + str(avg_difference)   
    GrtIncResult = "\n Greatest Increase In Profits: " + str(MaxProfitMonth) + " ($" + str(max_profit) + ")"
    GrtDecResult = "\n Greatest Decrease In Profits: " + str(MinProfitMonth) + " ($" + str(min_profit) + ")"
    ResultPrint = TitleResult + TotalMonthResult + TotalResult + AvgChangeResult + GrtIncResult + GrtDecResult

"""output the results in csv file"""

txt_output = os.path.join(".", "Analysis", "ResultPyBank.txt")
with open(txt_output, 'w') as textfile:
    textfile.write(ResultPrint)
    print(ResultPrint)