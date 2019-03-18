# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 01:31:46 2019

@author: hrajr
"""
def find(arr):
    st = sorted(set(arr))
    dic= {}
    k=1
    for i in st:
        dic[i]=k
        k+=1;
    rt=[]
    for i in arr:
        rt.append(dic[i])
    print(rt)
find([10,5,1,3,3])