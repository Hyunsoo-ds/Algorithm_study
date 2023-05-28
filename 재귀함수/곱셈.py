def square(a,b,c):
    if(b in data.keys()):
        return data[b]
    elif(b % 2 == 0):
        data[b] = ((square(a,b/2,c) )**2) % c
        return data[b]
    else:
        data[b] = (square(a,(b//2+1),c)  * square(a, b//2,c)) % c
        return data[b]

A, B, C = list(map(int,input().split()))
data = {1:A}

print(square(A,B,C) % C)