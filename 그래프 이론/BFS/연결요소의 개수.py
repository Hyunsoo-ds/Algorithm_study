import sys
input = sys.stdin.readline 
from collections import deque

N, M = map(int,input().split())
edges = [[] for i in range(N+1)]

for i in range(M):
    a,b = map(int,input().split())
    edges[a].append(b)
    edges[b].append(a)

queue = deque()
visited = []
count = 0

for i in range(1,N+1):
    
    if i in visited:        
        continue
    else:
        curr = i
        visited.append(i)
        while(True):
            for j in edges[curr]:
                if(not(j in visited)):
                    queue.appendleft(j)
                    visited.append(j)
            if(len(queue) == 0):
                break
            else:
                curr = queue.pop()
            
        count +=1

print(count)