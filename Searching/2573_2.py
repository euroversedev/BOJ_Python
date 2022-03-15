import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split()))
        for _ in range(N)]

# 빙산만 따로 저장 (최대 만개)
iceburg = dict()
for i in range(N):
    for j in range(M):
        if board[i][j] > 0:
            # 좌표와 빙산의 높이를 해시
            iceburg[(i, j)] = board[i][j]


# 빙산이 남아있는 동안 반복
cnt_year = 0
while iceburg:

    # 빙산의 덩어리 계산
    cnt_iceburg = 0
    visited = set(iceburg.keys())    # set에 포함되면 아직 방문하지 않음 
    for y, x in iceburg.keys():
        # 아직 방문하지 않았다면, BFS
        if (y, x) in visited:
            cnt_iceburg += 1
            
            q = deque([(y, x)])
            while q:
                i, j = q.popleft()
                
                for di, dj in [(1,0),(0,1),(0,-1),(-1,0)]:
                    if (i+di, j+dj) in visited:
                        q.append((i+di, j+dj))
                        visited.remove((i+di, j+dj))
    
    if cnt_iceburg >= 2:
        print(cnt_year)
        exit()
        
    # 각각의 빙산이 녹는 정도를 파악
    for (y, x), height in iceburg.items():
        cnt = 0
        for dy, dx in [(1,0),(0,1),(0,-1),(-1,0)]:
            ny, nx = y+dy, x+dx
            if board[ny][nx] == 0:
                cnt += 1
        iceburg[(y, x)] = height - cnt
    
    # 각각의 빙산 높이를 갱신
    for (y, x), height in list(iceburg.items()):
        if height > 0:
            board[y][x] = height
        else:
            board[y][x] = 0
            del iceburg[(y, x)]
    
    cnt_year += 1
    
print(0)

    
    