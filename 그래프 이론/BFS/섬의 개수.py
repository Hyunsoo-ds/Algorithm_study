from collections import *


def island(width,height,data):



w,h = map(int,input().split())

while(w != 0 and h != 0):
    island_data = []
    for i in range(h):
        island_data.append(list(map(int,input().split())))
    
    print(island(w,h, island_data))
    w,h = map(int,input().split())

    




