# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 22:57:39 2019

@author: hrajr
"""
dicLD={}
def LD(s, t):
    dd=dicLD.get(s+t,None)
    if(dd!=None):
        return dd
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1  
    res = min([LD(s[:-1], t)+1,
               LD(s, t[:-1])+1, 
               LD(s[:-1], t[:-1]) + cost])
    dicLD[s+t]=res
    return res
def fix(t,q):
    dic={}
    for qqa in q:   
        qs= qqa.split(" ")
        rs=''
        ct=0
        for qe in qs:
            tmp=qe
            for tgt in t:
                cost=LD(qe.lower(),tgt.lower())
                #print(cost)
                if(ct-cost<3):
                    ct+=cost
                    tmp=tgt        
            rs+=' '+tmp
        rs=rs.lower().strip()
        print(ct)
        if(ct>3):
            rs=qqa.lower()
        
        dic[rs]=dic.get(rs,0)+1
    vs=sorted(dic.keys())
    for k in range(len(vs)):
        print(vs[k],":%d"%dic[vs[k]],sep="",end="")
        if(k!=len(vs)-1):
            print("")
    if(len(vs)>=3):
        print("")
    # print(qqa,":%d"%cst)
def tc():
    n=int(input())
    t=[]
    for i in range (n):
       t.append(input())
    n=int(input())
    q=[]
    for j in range (n):
        q.append(input())
    fix(t,q)
#tc()
#fix(['technology','institute','business','school'],['ABC Intiute of Tecnology','XYZ Business School','ABC Intiute OF Technology'])
fix(['technology','institute','business','school'],['ABC Intiute of Tecnology','XYZ Business School','PPP Municipality SCHOOL'])

#     ABC Intiute of Tecnology

#XYZ Business School

#PPP Municipality SCHOOL  
 #  4
##technology
#institute
#business
#school
#3
#ABC Intiute of Tecnology
##XYZ Business School
#ABC Intiute OF Technology
