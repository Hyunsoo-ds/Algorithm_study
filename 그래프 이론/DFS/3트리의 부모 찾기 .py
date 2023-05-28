from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
edges = [[] for i in range(N+1)]

for i in range(N-1):
    a,b = map(int,input().split())
    edges[a].append(b)
    edges[b].append(a)

parent = [0]*(N+1)

visited = [True] * (N+1)
stack = deque()

stack.append(1)
visited.append(1)

while(len(stack) != 0):
    curr = stack.pop()
    for i in edges[curr]:
        if(visited[i]):   #여기서 not in 을 써버리면 배열의 모든 길이를 탐색하는 것이니까 n^2의 시간 복잡도가 걸리는거일 수도
            parent[i] = curr
            stack.append(i)
            visited[i] = False

print('\n'.join(map(str,parent[2:])))

