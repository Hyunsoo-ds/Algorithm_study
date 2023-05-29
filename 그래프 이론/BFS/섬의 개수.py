from collections import *

def move(curr,arrow,M,N):
    new = [curr[0] + arrow[0], curr[1] + arrow[1]]

    if(new[0] < 0 or new[1] < 0 or new[0] >= M or new[1] >= N):
        return False
    else:
        return new




def island(width,height,data):
    DIRECTIONS = ((1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1))
    count = 0
    
    visited = [[False] * width for _ in range(height)]

    for row in range(height):
        for col in range(width):
            if(not(visited[row][col]) and data[row][col] == 1):
                q = deque()
                q.append([row,col])
                visited[row][col] = True
                
                while(len(q) != 0):
                    curr = q.popleft()
                    for arrow in DIRECTIONS:
                        moved = move([curr[0],curr[1]],arrow,height,width)
                        if(moved):
                            r,c = moved
                            if(not(visited[r][c]) and data[r][c] == 1):
                                q.append(moved)
                                visited[r][c] = True
                count +=1
                

    return count





w,h = map(int,input().split())

while(w != 0 and h != 0):
    island_data = []
    for i in range(h):
        island_data.append(list(map(int,input().split())))
    
    print(island(w,h, island_data))
    w,h = map(int,input().split())