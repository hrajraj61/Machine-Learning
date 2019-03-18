import math
N,F,T=int(input()),int(input()),0
for i in range(N):
    T+=list(map(int,input().split()))[1]
print(math.ceil(T/F))



def cal(T,F):
    if(T%F==0):
        return T//F
    else:
        return T//F+1
N=int(input())
F=int(input())
T=0
for i in range(N):
    S,C=map(int,input().split())
    T+=C
print(T)
print(cal(T,F))

//This is The Coding Area
import math

N,F=int(input()),int(input())

Total=0

for i in range(N):

  	Cm=list(map(int,input().split(' ')))[1]
    
    Total+=Cm
    
print(int(math.ceil(Total/F)))