n,k = list(map(int,input().split()))

coins = []
count = 0

for i in range(n):
    coins.append(int(input()))



for c in coins[::-1]:
    if( (k // c) >= 1):
        count += k // c
        k = k % c

print(count)