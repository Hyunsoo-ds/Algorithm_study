global stack 
stack = []

def choose(s,e,n,nums):
    if(n == 0):
        print(' '.join(stack))
        del stack[len(stack)-1]
        return
    for i in range(s,e-n+2):
        stack.append(str(nums[i]))
        choose(i+1,e,n-1,nums) 
    if(len(stack) > 0): 
        del stack[len(stack)-1]

while(True):
    line = list(map(int,input().split()))
    n = line[0]
    if(n == 0):
        break
    choose(1,n,6,line)
    print()

