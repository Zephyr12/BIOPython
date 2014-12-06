def convertdatetodays(strDate):
    date = strDate.split(' ')[::-1]
    dayConv = [1,20,360,7200,144000]
    days = 0
    for i in range(0,len(date)):
        days += int(date[i])*dayConv[i]
    return days
def adjustdaysfromepoch(intDays):
    return intDays-convertdatetodays('13 20 7 16 2')
def daysfromepochtodate(intDays):
    days = intDays 
    #             j  f  m  a  m  j  j  a  s  o  n  d
    monthtable = [31,28,31,30,31,30,31,31,30,31,30,31]
    month = 0
    year = 2000
    
    while(not (days <= monthtable[month]) if not (year % 4 == 0) else not (days <= 29)):
        #print(days,month,year)
        if(year % 4 == 0 and month == 1):
            #curse you leap feburary!
            days -= 29
            month += 1
        else:
            days -= monthtable[month]
            month += 1
        
        if (month == 12):
            month = 0
            year += 1
    return ""+str(days)+" "+str(month+1)+" "+str(year)
print(daysfromepochtodate(adjustdaysfromepoch(convertdatetodays(raw_input("")))))
