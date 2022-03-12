import sys
from collections import deque

N, M , K, X = map(int, sys.stdin.readline().strip().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().strip().split())
    graph[u].append(v)
    
# bfs
answer_city = []
visited = [False] * (N+1)
visited[X] = True
q = deque([(X, 0)])    # node number, distance

while q:
    u, dis = q.popleft()
    
    if dis == K:
        answer_city.append(u)
        
    for v in graph[u]:
        if visited[v] == False:
            visited[v] = True
            q.append((v, dis+1))

print(*sorted(answer_city) if len(answer_city) > 0 else [-1], sep='\n')