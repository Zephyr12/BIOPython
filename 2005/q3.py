import time
def matchstr(s,m):
    if(s[:len(m)] == m):
	    return True
    return False

e2m = {
    "a":".-",
    "b":"-...",
    "c":"-.-.",
    "d":"-..",
    "e":".",
    "f":"..-.",
    "g":"--.",
    "h":"....",
    "i":"..",
    "j":".---",
    "k":"-.-",
    "l":".-..",
    "m":"--",
    "n":"-.",
    "o":"---",
    "p":".--.",
    "q":"--.-",
    "r":".-.",
    "s":"...",
    "t":"-",
    "u":"..-",
    "v":"...-",
    "w":".--",
    "x":"-..-",
    "y":"-.--",
    "z":"--.."
    }
m2e = {}
for e in e2m.keys():
    m2e[e2m[e]] = e

def e2mf(s):
    tot = ""
    for i in s:
        tot += e2m[i]
    return tot

def m2ef1(m,l):#brute-force
   # print (m,l)
    if(l == 1):#base case
        for i in m2e:
            #print i,m
            if(i == m):
                global perm
                print m2e[i]
                perm+=1
                time.sleep(0.05)
    else:
        for i in m2e:
            #print i,m
            if(matchstr(m,i)):
                f = l
                f -=1
                print m2e[i],
                m2ef1(m[len(i):],f)

                
while(True):
    perm = 0
    i = raw_input("")
    m2ef1(e2mf(i),len(i))
    print perm
