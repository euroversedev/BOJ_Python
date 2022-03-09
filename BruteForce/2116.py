import sys

N = int(input())
dice = [list(map(int, sys.stdin.readline().strip().split()))
       for _ in range(N)]

bottom_top = {0:5,5:0,1:3,3:1,2:4,4:2}

for i in range(6):
    bottom = i
    top = bottom_top[bottom]
    