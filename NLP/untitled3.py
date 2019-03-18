import sys
n=4
arr=[[0,3,9,6],
     [1,4,4,5],
     [8,4,5,2],
     [1,8,5,9]]
array=[False]
vm=sys.maxsize

def getSub(r,d,s):
    if r==n and d==n:
        k=min(vm,s)
        vm=k
    if r==n or d==n:
        return ;
    getSub(r+1,d,s+arr[r][d])
    getSub(r,d+1,s+arr[r][d])
    
    
print(getSub(0,0,0),vm)