n = int(input())      
reserve = dict()

for i in range(n):
    start,end = list(map(int,input().split(' ')))
    reserve[end] = start
print('---------<before>------------')
print('reserve:', reserve)

reserve = sorted(reserve.items())  #(종료 시각, 시작 시각)으로 구성된 "종료시각 기준"으로 정렬된 리스트

count = 0
finish_time = 0

print('--------<sorted>-------------')
print('reserve:', reserve)
for event in range(len(reserve)):
    #print('event:', event)
    if(finish_time <= reserve[event][1]):  #현재 종료시각 보다 다음 시작시간이 클때 
        count +=1
        finish_time = reserve[event][0]    # 횟수를 +1하고 finish_time을 다음 시작시간으로 교체합니다.
        #print(f'event{event} was taken')
        

print(count)
