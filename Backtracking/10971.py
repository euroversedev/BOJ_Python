import sys

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip().split())))
    
def dfs(visited, u, origin, depth, sum_):
    visited[u] = True
    
    if u == origin and depth == N:
        return sum_
    
    min_sum = 10**9
    for v, dis in enumerate(graph[u]):
        if visited[v] == False:
            min_sum = min(min_sum, dfs(visited, v, origin, depth+1, sum_+graph[u][v]))
            visited[v] = False
    
    return min_sum
    
    
min_ = 10**9
for i in range(N):
    visited = [False] * N
    cost = dfs(visited, i, i, 1, 0)
    min_ = min(min_, cost)
    
print(min_)