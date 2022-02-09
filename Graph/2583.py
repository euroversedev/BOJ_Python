import sys
from collections import deque

N, M, K = map(int, input().split())
board = [[0] * M for _ in range(N)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    
    for y in range(y1, y2):
        for x in range(x1, x2):
            board[y][x] = -1    # 직사각형의 위치

def bfs(i, j):
    area = 1
    board[i][j] = 1
    
    q = deque([(i, j)])
    while q:
        y, x = q.popleft()
        
        for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
            if 0<=y+dy<N and 0<=x+dx<M:
                if board[y+dy][x+dx] == 0:
                    board[y+dy][x+dx] = 1
                    q.append((y+dy, x+dx))
                    area += 1
    return area
    

result = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            area = bfs(i, j)
            result.append(area)

print(len(result))
print(*sorted(result))

''' [review]
영역의 넓이를 구하려면 DFS보다 BFS가 용이할 것 같아서
BFS로 풀었음. 문제 분류는 DFS로 되어있음.

dfs로 영역 구하려면
상위 재귀의 넓이 = 하위 재귀 넓이 + 하위 재귀 넓이 ...
이런식으로 코딩해야함
'''