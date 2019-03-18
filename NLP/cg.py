# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 10:25:04 2019

@author: hrajr
"""

def win(nlt,maxsum):
    for i in nlt:
        cmp=round(maxsum/2+0.1)+i
        if(cmp>maxsum):
            maxsum=cmp
    return maxsum

lt=list(map(int,input().split(',')))
ln=len(lt)
start=lt[ln-1]
nlt=lt[1:ln-1] 

print(win(nlt,start))
    

  
def getMaxWin(arr,money):
    for i in range(len(arr)):
        curr=round(money/2+0.1)+arr[i]
        if(curr>money): money=curr
    return money
arr=list(map(int,input().split(',')))
print(getMaxWin(arr[1:len(arr)-1],arr[len(arr)-1]))
    
    
    
import math
def rd(v):
    t=math.ceil(v)
    if(t-v<=0.5): return t
    else: return math.floor(v)
def find(arr,s):
    n=len(arr)
    prevs=s
    for i in range(n):
        t=rond(prevs/2)+arr[i]
       
        if(prevs<t):
            prevs=t
    print(prevs)
arr=list(map(int,input().split(",")))
n=len(arr)-1
brr=list(arr[1:n])
print(brr,arr[n])
find(brr,arr[n])




#9,8,6,4,3,9,2,5,8,6,2

        