n = int(input())

answer = 0

for i in range(1,n): 
    value = str(i)
    sum = i
    for j in range(len(value)):
        sum += int(value[j])
    if(sum == n):
        answer = i
        break


print(answer)
