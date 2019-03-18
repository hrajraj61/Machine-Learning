# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 00:37:20 2019

@author: hrajr
"""

# Python program for Dijkstra's single 
# source shortest path algorithm. The program is 
# for adjacency matrix representation of the graph 

# Library for INT_MAX 
import sys 
import math
  
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                      for row in range(vertices)] 
  
    def printSolution(self, dist): 
        print ("Vertex tDistance from Source")
        for node in range(self.V): 
            print( node,"t",dist[node] )
  
    # A utility function to find the vertex with  
    # minimum distance value, from the set of vertices  
    # not yet included in shortest path tree 
    def minDistance(self, dist, sptSet): 
  
        # Initilaize minimum distance for next node 
        min = sys.maxsize 
  
        # Search not nearest vertex not in the  
        # shortest path tree 
        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 
  
        return min_index 
  
    # Funtion that implements Dijkstra's single source  
    # shortest path algorithm for a graph represented  
    # using adjacency matrix representation 
    def dijkstra(self, src): 
  
        dist = [sys.maxsize] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V 
  
        for cout in range(self.V): 
  
            # Pick the minimum distance vertex from  
            # the set of vertices not yet processed.  
            # u is always equal to src in first iteration 
            u = self.minDistance(dist, sptSet) 
  
            # Put the minimum distance vertex in the  
            # shotest path tree 
            sptSet[u] = True
  
            # Update dist value of the adjacent vertices  
            # of the picked vertex only if the current  
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree 
            for v in range(self.V): 
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: 
                        dist[v] = math.floor(dist[u]/2) + self.graph[u][v] 
  
        self.printSolution(dist) 
  
def getGraph(arr,n):
    dic={}
    c=0
    nn=n*n
    for i in range(n):    
        for j in range(n):
            dic[i*(n)+j]=arr[i][j]
    emp=[[0]*nn for i in range(nn)]
    for i in range(n):
        for j in range(n):
            v=i*n+j
            r=(j+1)
            d=(i+1)
            if(r<n):
                emp[v][r+i*n]=arr[i][r]
            if(d<n):
                emp[v][d*n+j]=arr[d][j]
            
    return emp
def plot(arr,n,src_x,src_y,dest_x,dest_y):
    g=Graph(n*n)
    g.graph=getGraph(arr,n)
    print(g.graph)
    g.dijkstra(0)
    
# Driver program 
g = Graph(9) 
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
		[4, 0, 8, 0, 0, 0, 0, 11, 0], 
		[0, 8, 0, 7, 0, 4, 0, 0, 2], 
		[0, 0, 7, 0, 9, 14, 0, 0, 0], 
		[0, 0, 0, 9, 0, 10, 0, 0, 0], 
		[0, 0, 4, 14, 10, 0, 2, 0, 0], 
		[0, 0, 0, 0, 0, 2, 0, 1, 6], 
		[8, 11, 0, 0, 0, 0, 1, 0, 7], 
		[0, 0, 2, 0, 0, 0, 6, 7, 0] 
		]; 
def get(arr,r,d,n):
    if(r==n or d==n):
        return 0;
    if(r<n):
        g = get(arr,r+1,d,n)
    elif(d<n):
        g =min(g,get(arr,r,d+1,n))
    return math.floor(arr[r][d]/2)+g
arr=[[0,3,9,6],
     [1,4,4,5],
     [8,2,5,4],
     [1,8,5,9]]
#plot(arr,3,0,0,0,1)

print(get(arr,0,0,4))

    


#for k,g in enumerate(arr):print(k,g)
#g.dijkstra(0,7); 

# This code is contributed by Divyanshu Mehta 
