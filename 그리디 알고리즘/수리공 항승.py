N, L = list(map(int,input().split()))
nods = sorted(list(map(int,input().split())))

pointer = 0
count = 0

if(L != 1):
    for i in range(1,len(nods)):
        
        if((nods[i] - nods[pointer] +   1) > L):  
            count += 1
            pointer = i
    count +=1
else:
    count = N
  


print(count)


