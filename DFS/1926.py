import sys
sys.setrecursionlimit(10**9)

N, M = map(int, input().split())
board = [list(map(int, sys.stdin.readline().strip().split()))
        for _ in range(N)]
move = [(1,0), (0,1), (-1,0), (0,-1)]

def dfs(y, x):
    board[y][x] = 0
    
    size = 1
    for dy, dx in move:
        if 0<=y+dy<N and 0<=x+dx<M:
            if board[y+dy][x+dx] == 1:
                board[y+dy][x+dx] = 0
                size += dfs(y+dy, x+dx)
    
    return size


size_ = [0]
cnt = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            cnt += 1
            size_.append(dfs(i, j))

            
print(cnt)
print(max(size_))

''' [review]
500x500 인 경우, dfs(재귀)로 풀면
재귀가 쌓이면서 메모리 초과가 나온다. (재귀 스택오버플로우)
=> BFS로 풀자.
BFS 면적 구하기 == POP 몇번 하는지 세기

속도, 메모리 측면에서 dfs보다는 bfs가 우세하다. bfs 사용할 수 있으면 쓰자.
dfs는 백트래킹에나 잘 써먹자구.
'''
