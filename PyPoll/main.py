"""This python script reads lection_data.csv and finds the names of candidates, stores them in a list
and counts their votes, thus finds the winner. The results are output as ResultPyPoll1.txt """

import os
import csv
import operator
import numpy as np 

#add path for budget_data.csv file
poll_csv = os.path.join('.', 'Resources', 'election_data.csv')

#open csv.file in read mode

with open(poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

# create a list and dictionary to store data from csv file
    my_list = []
    my_dict = {}

# loop through csv, extract candidate names and store them in a list
    for row in csvreader:
        my_list.append(row[2])

# using the following line of code we can find the unique values in a list and sums its values
# this way we double check if there are other names that exist in the csv file
    result = list(zip(*np.unique(my_list, return_counts=True)))

#move results to dictionary as a value
    my_dict = dict(result)
    total_poll = len(my_list)
    
    max_value = 0
    max_key = None

#find max value in a dictionary
    for max in my_dict:
        if my_dict[max] > max_value:
            max_value = my_dict[max]
            max_key = max

#assign winner name 
    winner_name = max_key
    
#print the results
    TitleResult = "Election Results \n--------------------------"
    TotalVotes = "\nTotal votes: " + str(total_poll) + "\n--------------------------"
    KhanVotes = "\nKhan: " + str(round(my_dict['Khan']/total_poll * 100,3)) + "% " + "(" + str(my_dict['Khan']) + ")"
    CorreyVotes = "\nCorrey: " + str(round(my_dict['Correy']/total_poll * 100,3)) + "% " + "(" + str(my_dict['Correy']) + ")"
    LiVotes = "\nLi: " + str(round(my_dict['Li']/total_poll * 100,3)) + "% " + "(" + str(my_dict['Li']) + ")"
    OTooleyVotes = "\nCorrey: " + str(round(my_dict["O'Tooley"]/total_poll * 100,3)) + "% " + "(" + str(my_dict["O'Tooley"]) + ")" + "\n--------------------------"
    Winner = "\nWinner: " + str(winner_name) + "\n--------------------------"

    ResultPrint = TitleResult + TotalVotes + KhanVotes + CorreyVotes + LiVotes + OTooleyVotes + Winner

#output to csv file
txt_output = os.path.join(".", "Analysis", "ResultPyPoll.txt")
with open(txt_output, 'w') as textfile:
    textfile.write(ResultPrint)
    print(ResultPrint)
