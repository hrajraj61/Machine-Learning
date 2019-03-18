
def cal(child, values, curr, s):
     if(values[curr] + s > s and s > 0):  return s + values[curr]
     else:  return values[curr]
    
def find(child,values,curr,summ):
    maxm = summ = cal(child, values, curr, summ)
    for c in child[curr]:
        maxm = max(maxm, find(child, values, c, summ))
    return maxm

def bestSumDownwardTreePath(parent, values):  
    n =len(parent)
    child = [ [] for i in range(n)]
    for i in range(n):
        p = parent[i]
        if(not p == -1): child[p].append(i)
    return find(child, values, 0, values[0])
    
if __name__ == '__main__':
   #test(1)
   print("Ans:",bestSumDownwardTreePath([-1,0],[-5,-3]))
   print("Ans:",bestSumDownwardTreePath([-1,0,1,2,0],[-2,10,10,-3,10]))