from collections import deque

def move(curr,arrow,N):
    new = [curr[0] + arrow[0], curr[1] + arrow[1]]

    if(new[0] < 0 or new[1] < 0 or new[0] >= N or new[1] >= N):
        return False
    else:
        return new


N = int(input())

data = []


directions = [[1,0],[0,1],[-1,0],[0,-1]]



for i in range(N):
    data.append(list(map(int,input().split())))


max_height = max(map(max,data))
num_safe = [0]*(max_height+1)


for water in range(0,max_height):
    count = 0
    visited  = [[False]*N for _ in range(N)]

    for row in range(N):
        for col in range(N):
            #print(data[row][col],visited[row][col])
            if(data[row][col] > water and not(visited[row][col])): #물에 잠겼거나 방문한 곳은 제외 DFS 시작!
                stack = deque()     
                stack.append([row,col])
                visited[row][col] = True
                
                while(len(stack) != 0):
                    curr = stack.pop()
                    curr_r, curr_c  = curr 
                    #print('-------------')
                    #print('[curr]:',curr)            
                    for arrow in directions:          #주변 탐색
                        new = move([curr_r,curr_c],arrow,N)
                        #print('[new]:',new)
                        if(new):
                            r, c = new
                            if(data[r][c] > water and not(visited[r][c])):
                                #print('water_height', data[r][c])
                                #print('visited:',visited[r][c])
                                stack.append([r,c])
                                visited[r][c] = True
                count +=1
    num_safe[water] = count

print(max(num_safe))


