import sys

sys.setrecursionlimit(10**9)
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(i):
    visited[i] = True
    
    for j in graph[i]:
        if visited[j] == False:
            visited[j] = True
            dfs(j)

cnt = 0
for i in range(1, N+1):
    graph[i].sort()
    
    if visited[i] == False:
        dfs(i)
        cnt += 1
        
print(cnt)