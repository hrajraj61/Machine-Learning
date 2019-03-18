# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 01:30:39 2019

@author: hrajr
"""

def findShortestSubArray(nums):
        left, right, count = {}, {}, {}
        print([[i,x] for i,x in enumerate(nums)])
        for i, x in enumerate(nums):
            if x not in left: left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1
        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)
                print(ans)
        return ans
    
def findSA(arr):
    l,r,c={},{},{}
    for i,v in enumerate(arr):
        if v not in l: l[v] = i
        r[v]= i
        c[v]= c.get(v,0) + 1
    minm = len(arr)
    degree = max(c.values())
    for v in c:
        if c[v] == degree:
            minm = min(minm,r[v]-l[v] + 1)
    return minm
    
print(findShortestSubArray([1, 2, 2, 3, 1]))
#[1, 1, 2, 1, 2, 2]