import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(visited, u, depth):

    visited[u] = True
    
    if depth >= 5:
        return True
    
    for v in graph[u]:
        if visited[v] == False:
            if dfs(visited, v, depth+1):
                return True
            visited[v] = False
    
    return False

for i in range(N):
    visited = [False]*N
    if dfs(visited, i, 1):
        print(1)
        exit()
        
print(0)

''' review
bfs로 풀면 안됨.
4 4
0 1
1 2
2 3
3 0
이런 경우에 사이클이 발생해서 depth가 3으로 밖에 안나옴

특히, dfs를 돌고나서 visited[v]=False하는게 중요함.
다른 경로로 해당 노드를 다시 방문할 수 있기 때문.,
'''