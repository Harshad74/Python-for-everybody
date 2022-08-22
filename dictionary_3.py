name=input('enter a file:')
fhand=open(name)
count=dict()
for line in fhand:
    list=line.split()
    for key in list:
        count[key]=count.get(key,0)+1

bigword=''
bigcount=0
for x,y in count.items():
    if bigcount is None or bigcount<y:
        bigcount=y
        bigword=x
print(bigword,bigcount)




