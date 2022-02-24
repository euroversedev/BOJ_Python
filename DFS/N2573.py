import sys
import copy
from collections import deque
sys.setrecursionlimit(10**9)
N, M = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split()))
         for _ in range(N)]

def nextYear():
    tmp = [[0] * M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
                    if 0<=i+dy<N and 0<=j+dx<M and board[i+dy][j+dx] == 0:
                        tmp[i][j] += 1
    
    for i in range(N):
        for j in range(M):
            board[i][j] -= tmp[i][j]
            if board[i][j] < 0: board[i][j] = 0


def bfs(y,x,visited):
    visited[y][x] =True
    
    q = deque([(y,x)])
    while q:
        y, x = q.popleft()
        for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
            if 0<=y+dy<N and 0<=x+dx<M:
                if board[y+dy][x+dx] > 0 and visited[y+dy][x+dx]==False:
                    visited[y+dy][x+dx] = True
                    q.append((y+dy,x+dx))

def dfs(y, x, visited):
    visited[y][x] =True
    
    for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
        if 0<=y+dy<N and 0<=x+dx<M:
            if board[y+dy][x+dx] > 0 and visited[y+dy][x+dx]==False:
                dfs(y+dy,x+dx,visited)

def countIce():
    cnt = 0
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0 and visited[i][j] == False:
                bfs(i, j, visited)
                cnt += 1
    return cnt


year = 0
while True:
    year += 1
    nextYear()
    cnt = countIce()
    if cnt > 1:
        print(year)
        break
    if cnt == 0:
        print(0)
        break