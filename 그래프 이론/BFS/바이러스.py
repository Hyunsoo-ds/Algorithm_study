from collections import deque

N = int(input())

n_edges = int(input())

edges = [[] for _ in range(N+1)]


for i in range(n_edges):
    a,b = map(int,input().split())
    edges[a].append(b)
    edges[b].append(a)


visited = []

q = deque()
q.append(1)
visited.append(1)

while(len(q) != 0):
    curr = q.popleft()
    for related in edges[curr]:
        if(not(related in visited)):
            q.append(related)
            visited.append(related)


print(len(visited)-1)