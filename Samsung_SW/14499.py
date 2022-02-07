import sys

dice = [[0] * 3 for _ in range(4)]
N, M, x, y, K = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split()))
        for _ in range(N)]
cmds = list(map(int, sys.stdin.readline().strip().split()))

def move_right():
    global dice, board
    global x, y
    
    # 바깥으로 이동하는 경우 명령 무시
    if not (0<=x<N and 0<=y+1<M):
        return
    
    # dice 굴리기
    tmp = dice[1][0]
    dice[1][0] = dice[3][1]
    dice[3][1] = dice[1][2]
    dice[1][2] = dice[1][1]
    dice[1][1] = tmp
    
    if board[x][y+1] == 0:    # 이동한 칸에 쓰여 있는 수 == 0
        board[x][y+1] = dice[3][1]
        
    else:    # 이동한 칸에 쓰여있는 수 != 0
        dice[3][1] = board[x][y+1]
        board[x][y+1] = 0
    
    y = y + 1
    print(dice[1][1])

def move_left():
    global dice, board
    global x, y
    
    # 바깥으로 이동하는 경우 명령 무시
    if not (0<=x<N and 0<=y-1<M):
        return
    
    # dice 굴리기
    tmp = dice[1][0]
    dice[1][0] = dice[1][1]
    dice[1][1] = dice[1][2]
    dice[1][2] = dice[3][1]
    dice[3][1] = tmp
    
    if board[x][y-1] == 0:    # 이동한 칸에 쓰여 있는 수 == 0
        board[x][y-1] = dice[3][1]
        
    else:    # 이동한 칸에 쓰여있는 수 != 0
        dice[3][1] = board[x][y-1]
        board[x][y-1] = 0
    
    y = y - 1
    print(dice[1][1])
    
def move_up():
    global dice, board
    global x, y
    
    # 바깥으로 이동하는 경우 명령 무시
    if not (0<=x-1<N and 0<=y<M):
        return
    
    # dice 굴리기
    tmp = dice[0][1]
    dice[0][1] = dice[1][1]
    dice[1][1] = dice[2][1]
    dice[2][1] = dice[3][1]
    dice[3][1] = tmp
    
    if board[x-1][y] == 0:    # 이동한 칸에 쓰여 있는 수 == 0
        board[x-1][y] = dice[3][1]
        
    else:    # 이동한 칸에 쓰여있는 수 != 0
        dice[3][1] = board[x-1][y]
        board[x-1][y] = 0
    
    x = x - 1
    print(dice[1][1])

def move_down():
    global dice, board
    global x, y
    
    # 바깥으로 이동하는 경우 명령 무시
    if not (0<=x+1<N and 0<=y<M):
        return
    
    # dice 굴리기
    tmp = dice[3][1]
    dice[3][1] = dice[2][1]
    dice[2][1] = dice[1][1]
    dice[1][1] = dice[0][1]
    dice[0][1] = tmp
    
    if board[x+1][y] == 0:    # 이동한 칸에 쓰여 있는 수 == 0
        board[x+1][y] = dice[3][1]
        
    else:    # 이동한 칸에 쓰여있는 수 != 0
        dice[3][1] = board[x+1][y]
        board[x+1][y] = 0
    
    x = x + 1
    print(dice[1][1])

for cmd in cmds:
    if cmd == 1:
        move_right()
    elif cmd == 2:
        move_left()
    elif cmd == 3:
        move_up()
    elif cmd == 4:
        move_down()
    
    