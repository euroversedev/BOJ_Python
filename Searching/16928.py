import sys
from collections import deque

jump = dict()
N, M = map(int, sys.stdin.readline().strip().split())
for _ in range(N+M):
    u, v = map(int, sys.stdin.readline().strip().split())
    jump[u] = v
    
# bfs
visited = [False] * 101
visited[1] = True
q = deque([(1, 0)]) # num, depth

while q:
    now, depth = q.popleft()
    
    if now == 100:
        print(depth)
        exit()
    
    if now in jump:
        now = jump[now]
        visited[now] = True
    
    for i in range(1, 7):
        if now+i<=100 and visited[now+i] == False:
            visited[now+i] = True
            q.append((now+i, depth+1))