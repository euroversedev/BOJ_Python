import sys
import copy

N, M, T = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split()))
        for _ in range(N)]


# 내 공기청정기는 LG 퓨리케어 360도 알파
LG = []
dust = []
for i in range(N):
    if board[i][0] == -1: LG.append((i, 0))

time_now = 0
while True:
    new_board = [[0] * M for _ in range(N)]
    for y, x in LG: new_board[y][x] = -1
    
    # 미세먼지 확산
    for y in range(N):
        for x in range(M):
            if board[y][x] > 0:
                k = board[y][x] // 5
                # 각 먼지의 확산 가능 구역 구하기
                tmp = 0
                for dy, dx in [(1,0),(0,1),(0,-1),(-1,0)]:
                    if 0<=y+dy<N and 0<=x+dx<M and board[y+dy][x+dx] != -1:
                        new_board[y+dy][x+dx] += k
                        tmp += 1

                new_board[y][x] += board[y][x] - k * tmp
        
    # board = copy.deepcopy(new_board)
    board = new_board

    # 위쪽 공기청정기 가동
    LGY, LGX = LG[0][0], LG[0][1]    # (2, 0)
    for i in range(LGY-2, -1, -1):
        board[i+1][0] = board[i][0]
        
    for j in range(1, M):
        board[0][j-1] = board[0][j]
    
    for i in range(1, LGY+1):
        board[i-1][M-1] = board[i][M-1]
        
    for j in range(M-2, 0, -1):
         board[LGY][j+1] = board[LGY][j]
    
    board[LGY][LGX+1] = 0
    
    # 아래쪽 공기청정기 가동
    LGY, LGX = LG[1][0], LG[1][1]    # (3, 0)
    for i in range(LGY+2, N):
        board[i-1][0] = board[i][0]
        
    for j in range(1, M):
        board[N-1][j-1] = board[N-1][j]
        
    for i in range(N-2, LGY-1, -1):
        board[i+1][M-1] = board[i][M-1]
        
    for j in range(M-2, 0, -1):
        board[LGY][j+1] = board[LGY][j]
    
    board[LGY][LGX+1] = 0

    # 종료 조건
    time_now += 1
    if time_now == T:
        break
        

print(sum(map(sum, board)) + 2)