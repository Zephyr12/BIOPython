#Question 1
from math import *
def clock(minFast,hours):
    hTot = 0
    mTot = 0 
    for i in range(0,hours):
        hTot += 1
        mTot += minFast
    hTot += mTot / 60
    mTot = mTot % 60
    return str(1000+hTot%24)[2:] + ":" + str(1000+mTot)[2:]

#print clock(31,2)
marking = True
while(marking):
    solved = False
    s = raw_input("").split()
    m1 = int(s[0])
    m2 = int(s[1])

    ans = 0
    while(not solved):
        ans += 1
        #print ans
        if(clock(m1,ans) == clock(m2,ans)):
            print clock(m1,ans) #+ " " + clock(31,ans)
            solved = True
    

