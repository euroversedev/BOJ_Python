import sys

N, M = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split()))
        for _ in range(N)]

# CCTV 정보를 저장 (y, x, 기종)
CCTV = []
for y in range(N):
    for x in range(M):
        if 1<= board[y][x] <= 5:
            CCTV.append((y, x, board[y][x]))
        
def cnt_zero(board):
    cnt = 0
    for y in range(N):
        for x in range(M):
            if board[y][x] == 0:
                cnt += 1
    return cnt
        
# 각 CCTV의 방향을 바꿔가면서 완전 탐색
def dfs(board, depth):
    # 모든 CCTV의 방향이 결정되었으면 사각지대의 크기를 계산
    if depth == len(CCTV):
        min_size = min(min_size, cnt_zero(board))
        return
    
    y, x, num = CCTV[depth+1]
    
        
    
    
