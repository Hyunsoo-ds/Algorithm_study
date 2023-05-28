def judge(num,correct):
    num = str(num)
    correct = str(correct)
    strike = 0
    ball = 0

    for i in range(3):
        for j in range(3):
            if(num[i] == correct[j]):
                if(i == j):
                    strike +=1
                else:
                    ball +=1
    
    return [strike,ball]


length = int(input())
answer = []
key = 0

for i in range(length):
    answer.append(list(map(int,input().split(' '))))

for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if(i == j or j == k or k == i):
                continue
            num = 100*i + 10*j+ k

            flag = True
            for condition in answer:
                if(judge(num,condition[0]) != condition[1:]):
                    flag = False
            if(flag):
                key +=1
    
print(key)



