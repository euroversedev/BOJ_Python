import sys
sys.setrecursionlimit(10**9)

N = int(input())
graph = [[] for _ in range(N+1)]
parents = [None] * (N+1) 
for _ in range(N-1):
    v1, v2 = map(int, sys.stdin.readline().strip().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
    
def dfs(u, parent):
    parents[u] = parent
    
    for v in graph[u]:
        if parents[v] == None:
            dfs(v, u)
dfs(1, 0)
print(*parents[2:], sep='\n')