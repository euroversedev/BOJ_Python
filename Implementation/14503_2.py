import sys

N, M = map(int, sys.stdin.readline().strip().split())
y, x, d = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split()))
        for _ in range(N)]


# 북0 동1 남2 서3
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 동서남북 모두 청소 or 벽인지 확인
def all_clear(y, x):
    result = True
    
    # 0이 존재하면 False
    for dy, dx in move:
        if 0<=y+dy<N and 0<=x+dx<M:
            if board[y+dy][x+dx] == 0:
                result = False
    
    return result

# 현재 뒤가 벽이면 True
def is_back_wall(y, x, d):
    result = True
    dy = move[d][0]
    dx = move[d][1]
    
    
    if 0<=y-dy<N and 0<=x-dx<M:
        if board[y-dy][x-dx] in [0, 2]:
            result = False
    return result
    

# 북0 동1 남2 서3
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]


k = 5
while True:
    print(*board, sep='\n')
    # 현재 위치 청소
    k += 1
    board[y][x] = k
    
    # 종료 조건 판별
    if all_clear(y, x) and is_back_wall(y, x, d):
        break
        
    elif all_clear(y, x) and not is_back_wall(y, x, d):
        dy = move[d][0]
        dx = move[d][1]
        if 0<=y-dy<N and 0<=x-dx<M:
            y, x = y-dy, x-dx
        continue
    
    # 왼쪽으로 돌기
    d = (d-1) % 4
    dy = move[d][0]
    dx = move[d][1]
    
    if 0<=y+dy<N and 0<=x+dx<M:
        # a`
        if board[y+dy][x+dx] == 0:
            y, x = y+dy, x+dx
        # b
        continue

cnt = 0

for i in range(N):
    for j in range(M):
        if board[i][j]==2:
            cnt += 1
print(cnt)

''' [review]
벽 1
청소 가능한 곳 0
청소 이미 한 곳 2
'''