fhand=open(r'C:\Users\JITENDRA\Desktop\Git\pythonfiles\abc.txt','r')
ch=fhand.read()
print(len(ch))

print(ch[:20])


fhand=open(r'C:\Users\JITENDRA\Desktop\Git\pythonfiles\abc.txt','r')
for line in fhand:
    if line.startswith('from'):
        line=line.rstrip()
        print(line)
