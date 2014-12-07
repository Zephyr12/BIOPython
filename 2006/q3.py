'''[20/25]'''
def ds(target,no,current):
    if(current == None):
        current =0
    if(no == 1):#last drat
        for i in range(1,21):
            if(current+i == target):
                #print str(current) + " + "+ str(i) + "=" + str(current+i)
                global tot
                tot += 1
    elif(current!=0):#middle drats
        for i in range(1,21):
            if(current+i < target):#second onwards
                #print str(current) + " + "+ str(i) + "=" + str(current+i),
                t = no - 1
                ds(target,t,current+i)
    else:#first drat
        
        for i in range(1,21):
            if(current+(i*2) < target):
                #print str(current) + " + "+ str(i) + "=" + str(current+(2*i)),
                t = no - 1
                ds(target,t,current+(2*i))
while(True):
    target = int(raw_input(""))
    drats = int(raw_input(""))
    tot = 0
    ds(target,drats,0)
    print tot 
