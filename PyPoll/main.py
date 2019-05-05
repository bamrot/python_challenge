import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')

#definition
data=[]
candidate_list=[]
candidate_vote=dict()
line='-------------------------'

#open
with open(csvpath,newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    header = next(csvreader)
    data=list(csvreader)

    total_votes=len(data)

    for record in data:
        candidate=record[2]
        voterID, country, name=record
        candidate_vote[name]=candidate_vote.get(name,0)+1

    #https://developers.google.com/edu/python/dict-files used "key"
    winner=max(candidate_vote, key=candidate_vote.get)

    print('election results')
    print(line)
    print('total_votes:{}'.format(total_votes)) #https://www.learnpython.org/en/String_Formatting
    print(line)

    for name, votes in candidate_vote.items():
        percentage=votes/total_votes * 100
        print('{0}:{1:.3f}% ({2})'.format(name, percentage, votes))

    print(line)
    print('Winner:{}'.format(winner))
    print(line)

#printing
output=(f'''Election Results
------------------
Total Votes:{(format(total_votes))}
Winner:{(format(winner))}
''')

print(output)

with open("output.txt",'w') as file:
    file.write(output)