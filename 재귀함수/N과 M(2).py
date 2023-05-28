

global stack 
stack = []

def choose(s,e,n):
    if(n == 0):
        print(' '.join(stack))
        del stack[len(stack)-1]
        return
    for i in range(s,e-n+2):
        stack.append(str(i))
        choose(i+1,e,n-1) 
    if(len(stack) > 0): 
        del stack[len(stack)-1]


M,N = map(int,input().split())
choose(1,M,N)