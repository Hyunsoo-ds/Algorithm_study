from queue import Queue

n = int(input())

a = Queue(list(range(1,n+1)))

while(a.qsize() != 1): 
    print(a.qsize())
    a.get()
    a.put(a.get())


print(a[0]) 