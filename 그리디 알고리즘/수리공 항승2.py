N, L = list(map(int,input().split()))
nods = sorted(list(map(int,input().split())))

left = L
count = 0
tape_is_on = False

for i in range(1,1001):
    if(i in nods):
        tape_is_on = True
    if(tape_is_on):
        left -= 1
    if(left == 0):
        count +=1
        left = L
        tape_is_on = False

    if(i == 1000):
        if(tape_is_on):
            count += 1

print(count)


