from random import randint

biglistnum  = int(input("length of bigger list"))
smallerlistnum = int(input("length of smaller list"))
numtoadd = int(input("value to be added to initial bigger list"))
#print(biglistnum, smallerlistnum, numtoadd)
biggerlist = []
smallerlist = []
while len(smallerlist) < smallerlistnum:
    randomnum = randint(0, 10)
    smallerlist.append(randomnum)
#print(smallerlist)
newlist = []
biggerlist.append(smallerlist)
for i in biggerlist[0]:
    i+= numtoadd
    newlist.append(i)
#print(newlist)
biggerlist.append(newlist)
print(biggerlist)









"""while len(biggerlist) < biglistnum:
    randomnum = randint(0, 10)
    biggerlist.append(randomnum)
print(biggerlist)
smallerlist.append(biggerlist)
print(smallerlist)"""



