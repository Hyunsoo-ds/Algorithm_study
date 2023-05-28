from collections import deque
import sys
input = sys.stdin.readline 

stack = deque()

N = int(input())

for i in range(N):
    operator = list(input().split())
    if(operator[0] == 'push'):
        stack.append(int(operator[1]))
    elif(operator[0] == 'pop'):
        if(len(stack) == 0):
            print(-1)
        else:
            print(stack.pop())
    elif(operator[0] == 'size'):
        print(len(stack))
    elif(operator[0] == 'empty'):
        if(len(stack) == 0):
            print(1)
        else:
            print(0)
    elif(operator[0] == 'top'):
        if(len(stack) == 0):
            print(-1)
        else:
            value = stack.pop()
            print(value)
            stack.append(value)
        
