fhand=open(r'C:\Users\JITENDRA\Desktop\Git\pythonfiles\abc.txt','r')
di=dict()
for line in fhand:
    line=line.rstrip()
    list=line.split()
    for l in list:
        if l in di:
            di[l]=di.get(l,0)+1
        else:
            di[l]=1
print(di)

bigword=''
bigcount=0
for x,y in di.items():
    if y>bigcount or bigcount is None:
        bigcount=y
        bigword=x
print(bigword,bigcount)
