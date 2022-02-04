import sys
sys.setrecursionlimit(10**9)

def dfs(array, x, y, N, M):
    array[x][y] = 0
    
    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        if 0<=x+dx<N and 0<=y+dy<M:
            if array[x+dx][y+dy] == 1:
                dfs(array, x+dx, y+dy, N, M)
    

N = int(input())
for _ in range(N):
    M, N, K = map(int, input().split())
    array = [[0] * M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        array[Y][X] = 1
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if array[i][j] == 1:
                dfs(array, i, j, N ,M)
                cnt += 1
    print(cnt)
    
    
''' [review]

dfs를 사용하는 경우 recursion Error가 발생할 수 있음
해결방법 1. bfs로 바꿔서 재귀 사용안하기
해결방법 2. sys.setrecursionlimit(10**9)로 재귀 깊이 제한 변경
(참고: 백준 기본 재귀 깊이 제한은 1000이다.)
'''