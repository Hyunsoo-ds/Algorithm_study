def salt(data):
    if(len(data) == 1):
        return  data[0]
    elif(len(data) == 2):
        if(data[0] < data[1]):
            return [salt[0],salt[1]]
        else:
            return [salt[1],salt[0]]
    else:
        pivot = len(salt)//2  
        data = salt(data[0:pivot])+ [data[pivot]] + salt(data[pivot+1:])
        return data

n = int(input())
data = []
for i in range(n):
    data.append(int(input()))


print('\n'.join(map(str,data)))
