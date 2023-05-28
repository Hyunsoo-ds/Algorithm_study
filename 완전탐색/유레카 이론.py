a = int(input())
li = []
tri_num = []

for i in range(a):
    li.append(int(input()))


for n in range(2,51): # 49개
    tri_num.append(int(n*(n-1)/2))

for num in li:
    flag = 0
    for i in tri_num:
        for j in tri_num:
            for k in tri_num:
                if(i + j + k == num):
                    flag = 1
                    break
            if(flag):
                break
        if(flag):
            break
    print(flag)


