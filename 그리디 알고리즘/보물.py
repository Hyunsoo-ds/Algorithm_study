n = int(input())
a = sorted(list(map(int,input().split())))
b = sorted(list(map(int,input().split())),reverse=True)

sum = 0

for i in range(n):
    sum += (a[i] * b[i])

print(sum)

