name = input('Enter file:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split() #list
    for word in words:
        counts[word] = counts.get(word,0) + 1  #dict

bigcount = None
bigword = None
for word,count in counts.items():  #key, value
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
      
print('\n')        
print('Big word = ',bigword, '  Total count =', bigcount)