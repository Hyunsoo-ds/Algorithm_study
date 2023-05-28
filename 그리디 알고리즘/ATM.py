n = int(input())
li = sorted(list(map(int,input().split())))

all_sum = 0

for i in range(n):
    sum = 0
    for k in range(i+1):
        sum += li[k]
    all_sum += sum

print(all_sum)
