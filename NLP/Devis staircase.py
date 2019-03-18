sdt={1:1,2:2,3:4}
def countset(n):
    ch=sdt.get(n,0)
    if ch!=0: return ch
    sdt[n] = countset(n-1)+countset(n-2)+countset(n-3)   
    return sdt[n]
#for i in range(int(input())): print(countset(int(input())))
import math
print(round(math.cos(math.radians(30)),9))