import sys
from collections import deque

M, N = map(int, input().split())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def bfs():
    q = deque()
    
    for i in range(N):
        for j in range(M):
            if array[i][j] == 1:
                q.append((i,j))
    
    while q:
        y, x = q.popleft()
        
        for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
            if 0<=y+dy<N and 0<=x+dx<M:
                if array[y+dy][x+dx] == 0:
                    q.append((y+dy, x+dx))
                    array[y+dy][x+dx] = array[y][x] + 1

bfs()
MAX = max(map(max, array))

if any(0 in arr for arr in array):
    print("-1")
elif MAX == 1:
    print("0")
else:
    print(MAX - 1)

''' [review]
2차원 리스트 최대값 구하기
: MAX = max(map(max, array))

2차원 리스트에서 원소 포함 여부 확인하기
존재하지 않는지 => if all(0 not in arr for arr in array):
하나라도 존재하는지 => if any(0 in arr for arr in array):

'''