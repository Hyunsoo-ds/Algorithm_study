from collections import deque

N = int(input())
start,end = map(int,input().split())
num_edge = int(input())

edges = [[] for _ in range(N+1)]

for i in range(num_edge):               #인접 리스트 완성
    j,k = map(int,input().split())
    edges[j].append(k)
    edges[k].append(j)

stack = deque()
visited = [-1] * (N+1)

stack.append(start)
visited[start] = 0


while(len(stack) != 0):


    curr = stack.pop()
    if(curr == end):
        break
    for i in edges[curr]:       #DFS 탐색
        if(visited[i] == -1):
            stack.append(i)
            visited[i] = visited[curr]+1


print(visited[end])

