import sys
from collections import deque
import copy

N = int(input())
array = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
max_height = max(map(max,array))

def bfs(array, i, j, rain):
    q = deque()
    q.append((i, j))
    
    while q:
        y, x = q.pop()
        
        for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
            if 0<=y+dy<N and 0<=x+dx<N:
                if array[y+dy][x+dx] > rain:
                    q.append((y+dy, x+dx))
                    array[y+dy][x+dx] = rain

def solution(array, rain):    # i 이하의 빗물은 잠김 => i 이상의 영역을 찾아냄
    
    cnt = 0
    for i in range(N):
        for j in range(N):
            if array[i][j] > rain:
                bfs(array, i, j, rain)
                cnt += 1
    
    return cnt

max_cnt = 0
for i in range(max_height):
    cnt = solution(copy.deepcopy(array), i)
    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)