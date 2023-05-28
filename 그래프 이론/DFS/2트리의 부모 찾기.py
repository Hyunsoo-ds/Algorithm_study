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

stack = deque()

stack.append(1)

while(len(stack) != 0):
    curr = stack.pop()
    print('curr:', curr)
    for i in edges[curr]:
            parent[i] = curr
            stack.append(i)

print('\n'.join(map(str,parent[2:])))

