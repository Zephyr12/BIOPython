''' ________________________________________
    score : [28/30]
    1b)def fac(i):
	tot = 1
	for x in range(i,1,-1):
		tot *= x
	return tot
      3! == [6]
      abc
      acb
      bac
      bca
      cab
      cba
    1c) 113
        122
        131
        
        221
        212

        311
        [6]
    ________________________________________'''

def w2t(word):#turns a word into a letter frequency table
    table = {}
    for i in word.upper():
        if(i in table):
            table[i] += 1
        else:
            table[i] = 1
    return table
#to help with marking[removed on handin]
while(True):
    s1 = raw_input("")
    s2 = raw_input("")
    print "Anagrams" if w2t(s1)==w2t(s2) else "Not anagrams"
