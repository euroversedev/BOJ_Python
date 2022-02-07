import sys

N, M = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split()))
        for _ in range(N)]

# CCTV의 위치
cctvs = []
for i in range(N):
    for j in range(M):
        if 0<board[i][j]<6:
            cctvs.append((i, j))
len_cctvs = len(cctvs)
    
def check_blind():
    result = 0
    for i in range(N):
        for j in range(M):
            if board[N][M] == 0
                result += 1
    return result
    
# 모든 조합의 cctv를 살펴보기 위해 백트래킹
def dfs(i, j, cnt):
    if cnt == len_cctvs:
        print(*board, sep='\n')
        cb = check_blind()
        if cb < MIN: MIN = cb
    
    if board[i][j] == 1:
    
    
for cctv in cctvs:
    