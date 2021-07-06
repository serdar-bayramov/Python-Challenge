import os
import csv

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
    OTooley = counter4
    print(Khan_poll, Correy_poll, Li_poll, OTooley)


    


    #counter = 0
    #for row in csvreader:
    
        #if row[2] == "Khan":
            #print(len(row[0]))


        
        



    #TitleResult = "Election Results \n--------------------------"
    #TotalVotes = "\nTotal votes: " + str(poll_count) + "\n--------------------------"
    #print(TitleResult,TotalVotes)