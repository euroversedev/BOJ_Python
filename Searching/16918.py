import sys

Y, X, N = map(int, sys.stdin.readline().strip().split())

board = [list(sys.stdin.readline().strip())
        for _ in range(Y)]

for y in range(Y):
    for x in range(X):
        if board[y][x] == 'O':
            board[y][x] = 0

time_now = 1


while True:
    if time_now == N:
        break
    
    time_now += 1
    
    # 폭탄 설치부
    for y in range(Y):
        for x in range(X):
            if board[y][x] == '.':
                board[y][x] = time_now
                
    if time_now == N:
        break

    # 폭탄 폴발부
    time_now += 1
    tmp = []
    for y in range(Y):
        for x in range(X):
            if board[y][x] + 3 == time_now:
                for dy, dx in [(0,0), (1,0),(-1,0),(0,1),(0,-1)]:
                    if 0<=y+dy<Y and 0<=x+dx<X:
                        tmp.append((y+dy, x+dx))
    
    for i, j in tmp:
        board[i][j] = '.'
    
    if time_now == N:
        break

for y in range(Y):
    for x in range(X):
        if board[y][x] != '.':
            board[y][x] = 'O'
            
for i in range(Y):
    print(''.join(board[i]))