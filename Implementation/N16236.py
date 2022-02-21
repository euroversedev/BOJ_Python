import sys
from collections import deque

N = int(input())
board = [list(map(int, sys.stdin.readline().strip().split()))
        for _ in range(N)]
shark_size = 2

breaker = False
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            y, x = i, j
            board[i][j] = 0
            breaker = True
            break
    if breaker: break

def bfs(visited, y, x, shark_size):
    q = deque([(y, x, 0)])
    
    min_dis = 10**9
    target = (y, x, 0)
    origin = (y, x)
    
    while q:
        y, x, distance = q.popleft()
        visited[y][x] = True
        
        if min_dis < distance:
            break
        
        if 0 < board[y][x] and distance <= min_dis:
            flag = False
            if y < target[0]:
                flag = True
                
            elif y == target[0] and x < target[1]:
                flag = True
            
            if flag:
                min_dis = distance
                target = (y, x, distance)
            
            
            
        for dy, dx in [(-1,0),(0,-1),(0,1),(1,0)]:
            ny, nx = y+dy, x+dx
            if 0<=ny<N and 0<=nx<N:
                if visited[ny][nx] == False:
                    # 자기 자신과 같거나 작으면 이동 가능
                    if board[ny][nx] <= shark_size:
                        q.append((ny, nx, distance +1))
                    
    return target
                
cnt = 0
time = 0
while True:

    print(*board, sep='\n')
    print()
    # bfs로 이동 가능한 가장 가까운 칸을 return
    visited = [[False] * N for _ in range(N)]
    target = bfs(visited, y, x, shark_size)
    
    if target[:2] == (y, x): break
    # target 방문하고 다시 반복
    time += target[2]
    print(target[2])
    (y, x, _) = target
    board[y][x] = 0
    cnt += 1
    
    
    if cnt == shark_size:
        shark_size += 1
        cnt = 0
    print(shark_size)
print(time)

    
    

    