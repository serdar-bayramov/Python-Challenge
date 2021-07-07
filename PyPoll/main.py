import os
import csv
import operator

#add path for budget_data.csv file
poll_csv = os.path.join('.', 'Resources', 'election_data.csv')

#open csv.file in read mode"""

with open(poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
   
    #polls = list(csvreader)
    #poll_count = len(polls)

    list_VoterID = []
    list_County = []
    list_Candidate = []
    winner = {}

    for row in csvreader:
        list_VoterID.append(row[0])
        list_County.append(row[1])
        list_Candidate.append(row[2])
    
    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0

    for cand in list_Candidate:
        if cand == "Khan":
            counter1 = counter1 + 1
    Khan_poll = counter1
    
    for cand in list_Candidate:
        if cand == "Correy":
            counter2 = counter2 + 1
    Correy_poll = counter2

    for cand in list_Candidate:    
        if cand == "Li":
            counter3 = counter3 + 1
    Li_poll = counter3
        
    for cand in list_Candidate:
        if cand == "O'Tooley":
            counter4 = counter4 + 1
    OTooley_poll = counter4


    total_poll = Khan_poll + Correy_poll + Li_poll + OTooley_poll

    Khan_percentage = round(int(Khan_poll)/int(total_poll) * 100,3)
    Correy_percentage = round(int(Correy_poll)/int(total_poll) * 100,3)
    Li_percentage = round(int(Li_poll)/int(total_poll) * 100,3)
    OTooley_percentage = round(int(OTooley_poll)/int(total_poll) * 100,3)
    
    winner["Khan"]=Khan_poll
    winner["Correy"]=Correy_poll
    winner["Li"]=Li_poll
    winner["O'Tooley"] = OTooley_poll
    winner_poll = max(winner.items(), key=operator.itemgetter(1))[0]
    

    TitleResult = "Election Results \n--------------------------"
    TotalVotes = "\nTotal votes: " + str(total_poll) + "\n--------------------------"
    KhanVotes = "\nKhan: " + str(Khan_percentage) + "% " + "(" + str(Khan_poll) + ")"
    CorreyVotes = "\nCorrey: " + str(Correy_percentage) + "% " + "(" + str(Correy_poll) + ")"
    LiVotes = "\nLi: " + str(Li_percentage) + "% " + "(" + str(Li_poll) + ")"
    OTooleyVotes = "\nO'Tooley: " + str(OTooley_percentage) + "% " + "(" + str(OTooley_poll) + ")" + "\n--------------------------"
    Winner = "\nWinner: " + str(winner_poll) + "\n--------------------------"

    ResultPrint = TitleResult + TotalVotes + KhanVotes + CorreyVotes + LiVotes + OTooleyVotes + Winner

txt_output = os.path.join(".", "Analysis", "ResultPyPoll.txt")
with open(txt_output, 'w') as textfile:
    textfile.write(ResultPrint)
    print(ResultPrint)