target = input()
op = target[::-1]

best = 0

for i in range(1,len(target)+1):
    #print('i:', i)
    count = 0
    for j in range(i):
        #print(f'comparing->{target[-(i)+j]} == {op[j]} ')
        if(target[-(i)+j] != op[j]):  
            break
        count += 1
    if(count > best):
        best = count
    #print('count:',count)


print(2*len(target) - best)

