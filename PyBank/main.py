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
    
    for row in csvreader:
        
        month_counter = month_counter + 1
        total += int(row[1])
        
        month_list.append(row[0])
        profit.append(row[1])

    difference = [int(y) - int(x) for x, y in zip(profit, profit[1:])]
    avg_difference = round(sum(difference)/len(difference), 2)
    
    #print(max_profit)
    for month, max_profit in zip(month_list,profit):
        max_profit = max(difference)
        index_max = difference.index(max_profit)
        MaxProfitMonth = month_list[index_max+1]
              
    for month, min_profit in zip(month_list,profit):
        min_profit = min(difference)
        index_min = difference.index(min_profit)
        MinProfitMonth = month_list[index_min+1]


    TitleResult = "Financial Analysis \n--------------------------"
    TotalMonthResult = "\n Total months: " + str(month_counter)
    TotalResult = "\n Total: " + str(total)
    AvgChangeResult = "\n Average Change: " + "$" + str(avg_difference)   
    GrtIncResult = "\n Greatest Increase In Profits: " + str(MaxProfitMonth) + " ($" + str(max_profit) + ")"
    GrtDecResult = "\n Greatest Decrease In Profits: " + str(MinProfitMonth) + " ($" + str(min_profit) + ")"
    ResultPrint = TitleResult + TotalMonthResult + TotalResult + AvgChangeResult + GrtIncResult + GrtDecResult

txt_output = os.path.join(".", "Analysis", "ResultPyBank.txt")
with open(txt_output, 'w') as textfile:
    textfile.write(ResultPrint)
    print(ResultPrint)