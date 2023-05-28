def sort(target):
    reserve = target
    for i in range(len(reserve)):    # 끝나는 시간 순으로 정렬
            best = i
            for j in range(i,len(reserve)):
                if(reserve[j][1] < reserve[best][1]):
                    best = j
            out = reserve[i]

            reserve[i] = reserve[best]
            reserve[best] = out

    return reserve

n = int(input())
reserve = []

for i in range(n):
    reserve.append(list(map(int,input().split(' '))))

reserve = sort(reserve)

count = 0

for p in range(len(reserve)):
    if(len(reserve) == 0):
        break

    finish_time = reserve[0][1]
    del reserve[0]
    count +=1

    if(len(reserve) == 0):
        break

    copy = reserve[:]
    for i in copy:
        if(i[0] < finish_time):
            del reserve[reserve.index(i)]

print(count)



            


