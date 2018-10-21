Christoss-MacBook-Pro:UCSD201809DATA4 ChristosKorgan$ pwd
/Users/ChristosKorgan/Desktop/Boot Camp/datarepo/UCSD201809DATA4
"""
"""
import csv
data=[]
voterid=[]
country =[]
candidate = []
with open('Resources/election_data.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        i=', '.join(row).split(',')
        voterid.append(i[0])
        country.append(i[1])
        candidate.append(i[2])

voterid=voterid[1:]
country =country[1:]
candidate = candidate[1:]

total_votes=len(voterid)
candidate_unique=set(candidate)
candidate_unique_dict ={}
for i in candidate_unique:
    candidate_unique_dict[i] = candidate.count(i)

candidate_unique_dict  =sorted(candidate_unique_dict.items(), key=lambda kv: kv[1],reverse=True)

with open('result.txt','a') as f:

    print('Election Results',file=f)


    print('.'*40,file=f)
    print('Total Months:',total_votes,file=f)
    print('.'*40,file=f)

    for k,v in candidate_unique_dict:
        percent = (v/total_votes*100.00)
        percent = '{:0.3f}'.format(percent)+'%'

        print(str(k.strip())+":", percent, '('+str(v)+')' ,file=f)


    print('.'*40,file=f)
    print('Winner: '+max(set(candidate), key=candidate.count),file=f)
    print('.'*40,file=f)


#printing the data again
print('Election Results')


print('-'*40)
print('Total Votes:',total_votes)
print('-'*40)

for k,v in candidate_unique_dict:
    percent = (v/total_votes*100.00)
    percent = '{:0.3f}'.format(percent)+'%'

    print(str(k.strip())+":", percent, '('+str(v)+')')


print('-'*40)
print('Winner: '+max(set(candidate), key=candidate.count))
print('.'*40)
