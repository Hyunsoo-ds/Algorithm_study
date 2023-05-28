zero = 0
plus = 0
minus = 0
degree = 0

def classify(value,add):
    global zero
    global plus
    global minus
    if(value == 1):
        plus +=add
    elif(value == -1):
        minus += add
    elif(value == 0):
        zero += add
    else:
        print('ERROR!!')

    return

def cut(data):
    global degree # test
    degree +=1
    L = len(data[0])

    if(L == 1):
        classify(data[0][0],1)
        return 0
    
    prev = data[0][0]
    flag = True

    for big in data:     # 요소둘이 모두 일치하는지 검사
        stop = False
        for small in big:
            if(prev != small):
                flag = False
                stop = True
                break
            else:
                prev = small
        if(stop):
            break
    if(flag):
        classify(data[0][0],1)
        return 0
    

    for column in range(0,L,L//3):    #9칸으로 cut 하기
        for row in range(0,L,L//3):
            sector = []
            for i in range(row, row + L//3):
               sector.append(data[i][column : column + L//3])
            cut(sector)

    return 0
N = int(input())


data = []

for i in range(N):
    data.append(list(map(int,input().split())))

cut(data)
print(minus,zero,plus,sep = '\n')

