x=[9,8,7]
x[2]=6
print(x)


d=dict()
d['csev']=2
d['cwen']=4
for k,v in d.items():
    print(k,v)


tups=d.items()
print(tups)


d={'a':10,'c':1,'b':22}
print(sorted(d.items()))

for k,v in sorted(d.items()):
    print(k,v)
