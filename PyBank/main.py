import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

data=[]
profit_loss=[]
list_profit_loss = []
previous_value = 0

#opening
with open(csvpath,newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    header = next(csvreader)
    record = list(csvreader)
    total_months = len(record)

    for row in record:
        amount = row[1]
        profit_loss.append(int(amount))
        profit_loss_gap=int(row[1])-previous_value
        previous_value=int(row[1])
        list_profit_loss.append(profit_loss_gap)
    final_list=list_profit_loss[1:]
    #results
    Total=sum(profit_loss)
    Average=sum(final_list)/len(final_list)
    increase=max(final_list)
    decrease=min(final_list)

#printing
output=(f'''financial analysis
------------------
Total months:{total_months}
Total:{Total}
Average change:{Average}
Greatest increase:{increase}
Greatest decrease:{decrease}''')

print(output)

with open("output.txt",'w') as file:
    file.write(output)
    




    
    


   







