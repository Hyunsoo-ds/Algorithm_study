def is_pelin(str):
    n = len(str)
    op = str[::-1]

    if(n%2 == 0): # n = 짝수
        if(str[0:int((n/2))] == op[0:int(n/2)]):
            #print(f'{str[0:int((n/2))]} : {op[0:int(n/2)]}')
            return n
    else:           # n = 홀수
        if(str[0:int((n-1)/2)] == op[0:int((n-1)/2)]):
            #print(f'{str[0:int((n-1)/2)]} : {op[0:int((n-1)/2)]}')
            return n
        
    return False

target = input()
op = target[::-1]

best = len(target+op)

for i in range(len(op)+1):
    n = is_pelin(target + op[i:])
    if(n and n < best):
        best = n


print(best)
    


