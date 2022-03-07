import sys
from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]

a, b = map(int, input().split())

M = int(input())
for _ in range(M):
    parent, child = map(int, sys.stdin.readline().strip().split())
    graph[parent].append(child)
    graph[child].append(parent)
    
def bfs(a, b):
    visited = [-1] * (N+1)
    visited[a] = 1
    q = deque([(a, 0)])
    
    while q:
        u, depth = q.popleft()
        
        for v in graph[u]:
            # 방문하지 않은 상태라면
            if visited[v] == -1:
                visited[v] = depth+1
                q.append((v, depth+1))
    
    return visited[b]

print(bfs(a,b))