import csv
import os
from Candidate import Candidate
from Ballot import Ballot

def main():
    filename = "results.csv"
    fields = []
    rows = []
    
    #Read voting data from a csv
    
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)

        fields = next(csvreader)

        for row in csvreader:
            rows.append(row)

    candidatesList = [] 


    #Traverse the 2D array, documenting all candidate names, and first choice vote count
    ballots = []
    
    for row in rows:
        candidates = []
        for x in range(1, len(row)):

            needToAddNew = True
            for candidate in candidatesList:
                if candidate.name == row[x]:
                    if(x == 1):
                        candidate.votes += 1
                    needToAddNew = False
                    
            if(needToAddNew and row[x] != ""):
                newCandidate = Candidate(row[x])
                if(x == 1):
                    newCandidate.votes += 1
                candidatesList.append(newCandidate)
            candidates.append(Candidate(row[x]))
        ballots.append(Ballot(candidates))
                

            
                
                

    #identify every candidate's vote share percent
    totalVotes = len(rows)
    for candidate in candidatesList:
        candidate.voteShare = candidate.votes / totalVotes
    
    #identify leading candidate(s)
    leadingCandidate,maxVoteShare = findHighestVoteShare(candidatesList)

    #if no candidate had greater than 50%, eliminate lowest candidate until a candidate has greater than 50%
    while(maxVoteShare <= 0.5):
        print("After last pass:")
        for candidate in candidatesList:
            print("Candidate: " + candidate.name + ". Vote Share: " + str(candidate.voteShare))
        losingCandidate = findLowestVoteShare(candidatesList)
        
        #When we eliminate a candidate we need to:
        #1) Set them as an invalid candidate
        #2) Re-evaluate all ballots accordingly
        #3) Calculate new vote shares and check for new max

        #1)
        for candidate in candidatesList:
        
            if(candidate.name == losingCandidate):
                candidate.valid = False
                #candidatesList.remove(candidate)
                
                del candidatesList[candidatesList.index(candidate)]
            
                break
        #2)
        for candidate in candidatesList:
            candidate.votes = 0

        for ballot in ballots:
            topCandidate = ballot.getTopValidCandidate([candidate.name for candidate in candidatesList])
            for candidate in candidatesList:
                if candidate.name == topCandidate:
                    candidate.votes += 1
                    break

        #3)
        for candidate in candidatesList:
            candidate.voteShare = candidate.votes / totalVotes

        leadingCandidate,maxVoteShare = findHighestVoteShare(candidatesList)

    print("Winner Found")
    for candidate in candidatesList:
        print("Candidate: " + candidate.name + ". Vote Share: " + str(candidate.voteShare))



        




    
            
        
def findHighestVoteShare(candidatesList):
    maxVoteShare = 0
    leadingCandidate = None
    for candidate in candidatesList:
        if candidate.voteShare > maxVoteShare:
            maxVoteShare = candidate.voteShare
            leadingCandidate = candidate.name

    return leadingCandidate, maxVoteShare

def findLowestVoteShare(candidatesList):
    leastVoteShare = 100
    losingCandidate = None
    for candidate in candidatesList:
        if candidate.voteShare < leastVoteShare:
            leastVoteShare = candidate.voteShare
            losingCandidate = candidate.name
    return losingCandidate
    


main()






