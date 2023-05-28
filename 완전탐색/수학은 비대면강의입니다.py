str = input()
arr = str.split(' ')
stop = False
for i in range(len(arr)):
    arr[i] = int(arr[i])

a,b,c,d,e,f = arr

answer = [0,0]

for x in range(-1000,1000):
    for y in range(-1000,1000):
        if((a*x + b * y == c) and (d*x + e*y == f)):
            answer = x,y
            stop = True
            break
    if(stop):
        break

print(answer[0], answer[1])

