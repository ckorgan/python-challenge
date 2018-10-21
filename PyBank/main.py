Christoss-MacBook-Pro:UCSD201809DATA4 ChristosKorgan$ pwd
/Users/ChristosKorgan/Desktop/Boot Camp/datarepo/UCSD201809DATA4
"""
"""
import csv
data=[]
with open('Resources/budget_data.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        data.append (', '.join(row))

date=[]
pro_loss =[]
type(date)
data=data[1:]
for i in data:
    date.append(i.split(',')[0])
    pro_loss.append(i.split(',')[1])

pro_loss =[ int(i.strip()) for i in pro_loss]
total_month=len(data)

total_pro_loss = sum(pro_loss)
greatestprofit = max(pro_loss)
greatestprofitdate = date[pro_loss.index(max(pro_loss))]
greatestloss = min(pro_loss)
greatestlossdate = date[pro_loss.index(min(pro_loss))]

print('Financial Analysis')
print('-'*40)
print('Total Months:',total_month)
print('Total: $'+str(total_pro_loss))
print('Greatest Increase in Profits:',greatestprofitdate,'($'+str(greatestprofit)+')')
print('Greatest Decreaes in Profits:',greatestlossdate,'($'+str(greatestloss)+')')

with open('results.txt','w') as f:
    print('Financial Analysis',file=f)
    print('.'*40,file=f)
    print('Total Months:',total_month,file=f)
    print('Total: $'+str(total_pro_loss),file=f)
    print('Greatest Increase in Profits:',greatestprofitdate,'($'+str(greatestprofit)+')',file=f)
    print('Greatest Decreaes in Profits:',greatestlossdate,'($'+str(greatestloss)+')',file=f)
