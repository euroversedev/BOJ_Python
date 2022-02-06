import sys

board = [list(map(int, sys.stdin.readline().strip().split()))
        for _ in range(9)]

def dfs(board, y, x):
    # board[y][x]는 현재 빈 칸인 상태,
    # 적절한 수를 찾아 집어넣고
    # 가로 세로 정사각형이 모두 채워진 경우 board[y][x]를 확정
    # 만약 채워지지 않은 경우 dfs로 처리하고 옴
    
    # 적절한 수 후보 li_
    tmp = []
    for i in range(9):
        tmp.append(board[y][i])
        tmp.append(board[i][x])
        
    for i in range((y//3)*3, ((y//3)+1)*3):
        for j in range((x//3)*3, ((x//3)+1)*3):
            tmp.append(board[i][j])
    
    li_ = []
    for i in range(1, 10):
        if i not in tmp:
            li_.append(i)
    
    
    # 적절한 수 집어 넣고
    for i in li_:
        board[y][x] = i
        
        # 가로 세로 정사각형에 빈 칸에 대해 dfs
        
        


''' [review]
설계:
빈 칸에 수를 채워넣고 확정하려면,
가로 세로 정사각형에 모든 수가 채워지도록 dfs하면 되지 않을까?
자신의 가로 세로 정사각형에 채워지지 않은 빈칸이 있으면
dfs를 돌리는 거지
'''