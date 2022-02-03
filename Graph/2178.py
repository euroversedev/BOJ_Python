import sys
from collections import deque

N, M = map(int, input().split())
array = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]


visited = [[False] * M for _ in range(N)]
def bfs(x, y, dist):
    q = deque()
    q.append((x, y, dist))
    visited[x][y] = True
    
    while q:
        i, j, dist = q.popleft()

        if i == N-1 and j == M-1:
            return dist
        
        for dx, dy in [(+1, 0), (-1, 0), (0, +1), (0, -1)]:
            if 0<=i+dx<N and 0<=j+dy<M:
                if (visited[i+dx][j+dy] == False) and (array[i+dx][j+dy] == 1):
                    q.append((i+dx, j+dy, dist+1))
                    visited[i+dx][j+dy] = True


result = bfs(0, 0, 1)
print(result)