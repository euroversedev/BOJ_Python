import sys
sys.setrecursionlimit(10**9)

N, M = map(int, input().split())
board = [list(map(int, sys.stdin.readline().strip().split()))
        for _ in range(N)]

visited = [[-1] * M for _ in range(N)]
def dfs(i, j):
    if (i, j) == (N-1, M-1):
        return 1
    
    if visited[i][j] >= 0:    # 방문한 적이 있다면 재활용
        return visited[i][j]
    
    visited[i][j] = 0
    
    for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
        ny, nx = i+dy, j+dx
        if 0<=ny<N and 0<=nx<M:
                if board[i][j] > board[ny][nx]:
                    visited[i][j] += dfs(ny, nx)
                    
    return visited[i][j]
    
print(dfs(0,0))

''' [review]
1987번과 마찬가지로
M과 N이 500 정도일 때 DFS로 모든 경우의 수를 찾으려고 하면
시간 초과가 나버림.
=> DP로 풀어야할 듯 1520_2.py (DP로 풀었음)

===> 다른 사람 풀이 보니까 dfs로도 풀리네?
아래는 내가 처음에 구현했던 dfs

visited = [[False] * M for _ in range(N)]
def dfs(i, j):
    if (i, j) == (N-1, M-1):
        return 1
    
    visited[i][j] = True
    
    cnt = 0
    for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
        if 0<=i+dy<N and 0<=j+dx<M:
            if visited[i+dy][j+dx] == False:
                if board[i][j] > board[i+dy][j+dx]:
                    cnt += dfs(i+dy, j+dx)
                    visited[i+dy][j+dx] = False
    return cnt
    
===> 아직 방문하지 않은 노드에 대해서 dfs로 경우의 수 구하고,
다른 경로에 대비해서 다시 방문하지 않은 노드로 바꿔놓을 경우 (끝에서 둘째줄)
이미 구했던 지점의 경우의 수를 처음부터 다시 구해야해서
계산할 것이 너무 많아짐.
대신에 => 인접한 모든 노드에 대해서 dfs돌리고,
이미 방문했던 노드에 방문한 경우, 자기가 앞전에 구해뒀던 경우의 수를 return

'''