from itertools import groupby
import time

def tr(a,lns):
    for i in range(1, max(a)):
        lns.append(''.join([ str(len(list(g))) + f for f, g in groupby(lns[i-1])]))
   # print(lns)
    #print(lns[max(a)-1])
    return [ sum([ int(j) for j in lns[i-1] ]) for i in a ] 

def tr1(a):
    n=len(a)
    t=''
    i=0
    while(i<n):
        k=str(a[i])
        count=1
        while(i+1<n and a[i+1]==a[i]):
            i+=1
            count+=1
        t+=str(count)+k
        i+=1
    return t 
def tr2(a):
    lns=['1']
    for i in range(1,max(a)):
        lns.append(tr1(lns[i-1]))
    #print (lns)
        

#print(tr1('21'))
#print(tr([1,2,7,54],['1']))
millis = int(round(time.time() * 1000))
print(tr([1,2,7,54],['1']))
print(- millis + int(round(time.time() * 1000)))
millis = int(round(time.time() * 1000))
#tr2([1,2,7,1])
print(- millis + int(round(time.time() * 1000)))

