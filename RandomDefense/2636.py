import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split()))
        for _ in range(N)]

time = 0

# 치즈의 위치 모두 구하기
cheese = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            cheese.append((i, j))
pre_cheese_cnt = len(cheese)    
# 외부 공기
air = deque([(0, 0)])
board[0][0] = 2

# 치즈가 있는 동안 반복
while cheese:
    
    # 외부 공기를 2로 표시
    while air:
        y, x = air.popleft()
        
        for dy, dx in [(1,0),(0,1),(0,-1),(-1,0)]:
            if 0<=y+dy<N and 0<=x+dx<M and board[y+dy][x+dx] == 0:
                board[y+dy][x+dx] = 2
                air.append((y+dy, x+dx))
    
    
    # 주변에 공기가 있는 치즈는 사라지고, 사라진 치즈는 공기로 바뀜
    tmp = []
    for y, x in cheese:
        flag = True
        for dy, dx in [(1,0),(0,1),(0,-1),(-1,0)]:
            if board[y+dy][x+dx] == 2:
                tmp.append((y, x))
                break
                
    for y, x in tmp:
        board[y][x] = 2
        air.append((y, x))
        del cheese[cheese.index((y,x))]
        
    time += 1
    if len(cheese) == 0:
        break
        
    # 한 턴이 지나고 나면 치즈 조각 저장
    pre_cheese_cnt = len(cheese)
    

print(time)
print(pre_cheese_cnt)