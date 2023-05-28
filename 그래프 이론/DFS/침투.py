from collections import deque

def move(curr,arrow,M,N):
    new = [curr[0] + arrow[0], curr[1] + arrow[1]]

    if(new[0] < 0 or new[1] < 0 or new[0] >= M or new[1] >= N):
        return False
    else:
        return new

M, N = map(int,input().split())
data = []
directions = [[1,0],[0,1],[-1,0],[0,-1]]


for i in range(M):
    data.append(list(map(int,list(input()))))

precolated = False

for col in range(N):
    if(data[0][col] == 0):
        visited = [[False]*(N) for _ in range(M)]
        stack = deque()

        stack.append([0,col])
        visited[0][col] = True

        while(len(stack) != 0):
            curr = stack.pop()
            if(curr[0] == M-1):
                precolated = True
                break

            for arrow in directions:
                new = move(curr,arrow,M,N)  
                if(new):
                    r, c = new
                    if(data[r][c] == 0 and not(visited[r][c])):
                        stack.append([r,c])
                        visited[r][c] = True

    if(precolated):
        break

if(precolated):
    print('YES')
else:
    print('NO')
        




