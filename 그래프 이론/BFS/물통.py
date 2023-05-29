from collections import deque

def pour(first,second,curr):
    global SIZE

    new_water = curr[:]

    s,d = curr[first],curr[second]
    S,D = SIZE[first], SIZE[second]

    if(s + d <= D):
        new_water[second] = s + d
        new_water[first] = 0
    else:
        new_water[first] = s- (D - d)
        new_water[second] = D
    
    return new_water




SIZE = list(map(int,input().split()))
water = [0,0,SIZE[2]]

visited = [[[False] * (SIZE[2]+1) for _ in range(SIZE[1]+1)] for _ in range(SIZE[0]+1)]


q = deque()
q.append([water[0],water[1],water[2]])
visited[water[0]][water[1]][water[2]] = True

possible = []

while(len(q) != 0):
    curr = q.popleft()

    if(curr[0] == 0 and not(curr[2] in possible)):                           #A == 0 이고 possible에 없을때만 append
        possible.append(curr[2])

    for i in range(3):                          # 주변 탐색
        for j in range(3):
            if(j != i):
                new = pour(i,j,curr)            #가능한 부을 수 있는 수에 대해서 각각 확인
                if(not(visited[new[0]][new[1]][new[2]]) ):
                    q.append(new)
                    visited[new[0]][new[1]][new[2]] = True


print(' '.join(list(map(str,sorted(possible)))))