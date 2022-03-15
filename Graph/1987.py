import sys

N, M = map(int, input().split())
board = [list(map(lambda x: ord(x)-ord('A'), sys.stdin.readline().strip())) for _ in range(N)]
visited = [False] * 26


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

max_ = 0
def dfs(i, j, sum_visited):
    global max_
    
    # 최대값 갱신
    if max_ < sum_visited:
        max_ = sum_visited
    
    for k in range(4):
        ny, nx = i+dy[k], j+dx[k]
        if 0<=ny<N and 0<=nx<M:
            if visited[board[ny][nx]] == False:
                visited[board[ny][nx]] = True
                dfs(ny, nx, sum_visited+1)
                visited[board[ny][nx]] = False

visited[board[0][0]] = True            
dfs(0, 0, 1)
print(max_)
    
