n = int(input())
roads = list(map(int,input().split()))
nods = list(map(int,input().split()))

min = nods[0]
distance = 0
price = 0

for i in range(1,n):
    distance += roads[i-1]
    if( min > nods[i] or i == n-1):
        price += min * distance
        min = nods[i]
        distance = 0

print(price)
