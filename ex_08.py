fhand=open('mbox-short.txt')
daylist=list()  # list
counts=dict()   # dictionary
for line in fhand:
    line=line.rstrip()
    words=line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    daylist.append(words[2])   
    print(words[2])
print(daylist)

for day in daylist :
    counts[day] = counts.get(day, 0) + 1
print(counts)