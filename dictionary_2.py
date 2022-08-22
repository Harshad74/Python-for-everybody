counts=dict()
line=input('enter a line of text:')
list=list()
list=line.split()
for name in list:
    counts[name]=counts.get(name,0)+1
print(counts)