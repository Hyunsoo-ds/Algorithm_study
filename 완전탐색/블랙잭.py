n,m = map(int,input().split(' '))
card = list(map(int,input().split(' ')))

key = m
answer = 0

for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            d = m - (card[i]+card[j]+card[k])
            if(d < key and d >= 0):
                key = d
            

print(m-key)