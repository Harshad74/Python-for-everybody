numlist=list()
while True:
    value=input('enter a number:')
    if value=='Done':
        break
    else:
        numlist.append(int(value))
avg=sum(numlist)/len(numlist)
print(avg)
