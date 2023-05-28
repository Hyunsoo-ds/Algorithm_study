N = int(input())
ropes = []
best = 0
for i in range(N):
    ropes.append(int(input()))

ropes.sort(reverse=True)

for i in range(N): # 0 ~ N-1
    score = ropes[i] * (i+1)
    if(score > best):
        best = score
    
print(best)