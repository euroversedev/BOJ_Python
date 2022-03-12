import sys
from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]

M = int(input())
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

# bfs
visited = [False] * (N+1)
visited[1] = True
q = deque([(1, 0)])

cnt = -1    # 자기 자신은 제외
while q:
    u, dis = q.popleft()
    if dis <= 2:
        cnt += 1
        
    for v in graph[u]:
        if visited[v] == False:
            visited[v] = True
            q.append((v, dis+1))
print(cnt)