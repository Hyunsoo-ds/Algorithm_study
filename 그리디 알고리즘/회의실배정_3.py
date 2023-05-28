n = int(input())        #sort 필요함, 그래도 시간 엄청 느림
reserve = dict()

for i in range(n):
    start,end = list(map(int,input().split(' ')))
    reserve[end] = start



reserve = sorted(reserve.items())

print('sorted:', reserve)

count = 0
finish_time = 0  #(end, start)
for i in reserve:
     if(finish_time <= i[1]):
          count +=1
          finish_time = i[0]

print(count)
