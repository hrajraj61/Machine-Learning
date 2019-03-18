# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 19:33:33 2019

@author: hrajr
"""

def find_max_sum(arr): 
    incl = []
    excl = []
    print(sum(excl) > sum(incl))
    new_excl=[]
    for i in range(len(arr)): 
        
        # Current max excluding i (No ternary in  
        # Python) 
        new_excl = list(excl) if sum(excl)>sum(incl) else list(incl) 
         
        # Current max including i 
        
        incl = list(excl)
        incl.append(arr[i])
        excl = list(new_excl) 
        print("i=",i)
        print("\texcl:",excl)
        print("\tincl:",incl)
        print("\tnew_excl",new_excl)
        print(" ")
      
    # return max of incl and excl 
    return (excl if excl>incl else incl) 
def find_max_sum1(arr): 
    incl = 0
    excl = 0
     
    for i in arr: 
          
        # Current max excluding i (No ternary in  
        # Python) 
        new_excl = excl if excl>incl else incl 
         
        # Current max including i 
        incl = excl + i 
        excl = new_excl 
      
    # return max of incl and excl 
    return (excl if excl>incl else incl)
            
print(find_max_sum([7, 6, 10, 100, 10, 5]))