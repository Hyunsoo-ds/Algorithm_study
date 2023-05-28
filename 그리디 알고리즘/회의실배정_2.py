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

n = int(input())        #sort 필요함, 그래도 시간 엄청 느림
reserve = []

for i in range(n):
    reserve.append(list(map(int,input().split(' '))))

reserve = sort(reserve)

count = 0
finish_time = 0
for i in reserve:
     if(finish_time <= i[0]):
          count +=1
          finish_time = i[1]

print(count)