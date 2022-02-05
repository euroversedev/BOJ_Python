import sys

# 입력
N = int(input())
K = int(input())
apples = [tuple(map(int, sys.stdin.readline().strip().split()))\
        for _ in range(K)]
L = int(input())
data = [tuple(sys.stdin.readline().strip().split())\
       for _ in range(L)]

# 뱀이 위치한 좌표는 1로 표시
# 사과가 위치한 좌표는 2
board = [[0] * N for _ in range(N)]
board[0][0] = 1
for y, x in apples:
    board[y-1][x-1] = 2

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction = 0
time = 0
y, x = 0, 0
tailY, tailX = 0, 0
while True:
    print(*board, sep='\n')
    
    
    for i in range(len(data)):
        if time == int(data[i][0]):    # 시간이 일치하면
            if data[i][1] == 'D':
                direction += 1
            else:
                direction -= 1
    
    dy, dx = d[direction]
    if 0<=y+dy<N and 0<=x+dx<N:
        if board[y+dy][x+dx] == 1:    # 자기 자신인 경우
            break
            
        flag = False
        if board[y+dy][x+dx] == 2:
            flag = True
        
        if flag:
            board[y+dy][x+dx] = 1
        else:
            board[tailY][tailX] = 0
            board[y+dy][x+dx] = 1
            tailY, tailX = tailY+dy, tailX+dx
        
        y, x = y+dy, x+dx

    
    else:
        break
        
    time += 1

print(time+1)