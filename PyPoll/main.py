"""This python script reads election_data.csv and finds the names of candidates, stores them in a list
and counts their votes, thus finds the winner. The results are output as ResultPyPoll.txt """

import os
import csv
from collections import Counter

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

#find unique values in the list and save in dictionary
    my_dict = dict(Counter(my_list).items())

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
    OTooleyVotes = "\nO'Tooley: " + str(round(my_dict["O'Tooley"]/total_poll * 100,3)) + "% " + "(" + str(my_dict["O'Tooley"]) + ")" + "\n--------------------------"
    Winner = "\nWinner: " + str(winner_name) + "\n--------------------------"

    ResultPrint = TitleResult + TotalVotes + KhanVotes + CorreyVotes + LiVotes + OTooleyVotes + Winner

#output to csv file
txt_output = os.path.join(".", "Analysis", "ResultPyPoll.txt")
with open(txt_output, 'w') as textfile:
    textfile.write(ResultPrint)
    print(ResultPrint)