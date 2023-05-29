from collections import *

N, K = map(int,input().split())

q = deque()
visited = [-1] * 100001
best = []


q.append(N)
visited[N] = 0

while(len(q) != 0):
    curr = q.popleft()
    #print('curr:',curr)
    #print('degree:',visited[curr])

    if(curr == K):
        print(visited[K])
        break
    moved = [curr -1, curr+1, curr*2]


    for new in moved:
        if(new > 100000 or new < 0):
            continue
        if(visited[new] == -1 ):
            q.append(new)
            star = K
            visited[new] = visited[curr] + 1        #검색할 때마다 차수 1 더해서 저장

