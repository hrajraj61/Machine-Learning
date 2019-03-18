import sys,math
n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]
class cell:
    def __init__(self,x,y,d):
        self.x=x
        self.y=y
        self.d=d
    def __lt__(self,other):
        if(self.d==other.d):
            if not(self.x == other.x):
                return self.x < self.x 
            else:
                return self.y < other.y 
        return self.d<other.d
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y and self.d==other.d
    def __hash__(self):
        return hash(self.x+self.y+self.d)
    def lessthan(self,cell1):
        if(self.d==cell1.d):
            if(self.x==cell1.x):
                return self.x<cell1.y
            else:
                return self.y<cell1.y
        return self.distance<cell1.distance
def isInside( i, j):
    return (i>=0 and i<n and j>=0 and j<n)
def shortest(arr,n):
    print(arr)
    dis=[[sys.maxsize]*n for i in range(n) ]
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    st=set()
    st.add(cell(0,0,0))
    dis[0][0]=arr[0][0]
    while(len(st)!=0):
        c =  next(iter(st))
        st.remove(c)
        for i in range(4):
            x=c.x + dx[i]
            y=c.y + dy[i]
            if(not isInside(x,y)):
                continue
            print(dis[x][y])
            print(x,y)
            if(dis[x][y]>dis[c.x][c.y]+arr[x][y]):
                if(not dis[x][y] == sys.maxsize):
                    st.remove(cell(x,y,dis[x][y]))
                dis[x][y]=math.floor((dis[c.x][c.y])/2)+arr[x][y]
                st.add(cell(x,y,dis[x][y]))
            
    return dis[n-1][n-1]

print(shortest(arr,n))
v="""
0 3 9 6
0::03::39::96::61 4 4 5
1::14::44::45::58 2 5 4
8::82::25::54::41 8 5 9
1::18::85::59::912"""


"""5
0 82 2 6 7
4 3 1 5 21
6 4 20 2 8
6 6 64 1 8
1 65 1 6 4
"""