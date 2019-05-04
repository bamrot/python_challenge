import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

### if it worked out it should have looked like 
with open(csvpath, newline='') as csvfile:

    ## CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    total_months = 0
    next(csvreader)

    for row in csvreader:
        print(row)
        total_months = 1+total_months
    
    print(total_months)








