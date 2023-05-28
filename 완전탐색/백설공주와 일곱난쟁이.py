li = []
sum = 0
stop = False

for i in range(9):
    value = int(input())
    sum += value
    li.append(value)


for i in range(len(li)):
    if(not(stop)):
        for j in range(i+1,len(li)):
            if(sum - (li[i] + li[j]) == 100):
                li[i] = '!'
                li[j] = '!'
                stop = True
                break

for i in li:
    if(not(i == '!')):
        print(i) 
