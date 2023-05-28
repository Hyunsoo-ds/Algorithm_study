def tri_area(a,b,c):
    area = 0.5 * abs( (a[0]*b[1] + b[0] * c[1] + c[0]*a[1] - (a[1]*b[0] + b[1]*c[0] + c[1]*a[0])) )
    return area

length = int(input())

max = 0

data = []
for i in range(length):
    data.append(list(map(int,input().split(' '))))



for i in range(0,length-2):
    for j in range(i+1, length-1):
        for k in range(j+1, length):
            area = tri_area(data[i],data[j],data[k])

            if(area > max):
                max = area

print(max)