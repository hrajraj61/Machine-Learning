# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 23:15:07 2019

@author: hrajr
"""

def keypad(keypad,text):
    keypad.append(' ')
    d ={ i[k] : k+1 for i in keypad for k in range(len(i)) }     
    m=1
    sset = [1,1,2,4,8,16]
    for j in text:
        m = (m*sset[d[j]]) % 1000000007
    return m
keys=["MGJ","YIZ","DKS","BHP","VENA","FLQ","URT","CWOX"]
print(keypad(keys,"MY NAME IS HRISHABH MY NAME IS HRISHABH MY NAME IS HRISHABH "))

print(*[i%2==0 for i in range(100) if i%2==0 ],sep='\n')