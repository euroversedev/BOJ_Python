import sys
from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()
    



''' DFS with Recursive Funcition(as Stack)
1. 해당 노드 방문처리
2. 인접 노드 중 하나를 골라서 dfs
'''
visited = [False] * (N+1)
def dfs(graph, start):
    visited[start] = True
    print(start, end=" ")
    
    nodes = graph[start]
    for node in nodes:
        if visited[node] == False:
            dfs(graph, node)

dfs(graph, V)
print()


''' BFS with Queue
1. 시작 노드 큐에 넣고
2. 반복문으로, 큐에서 POP하고
3. POP한 노드의 인접노드들을 모두 큐에 집어 넣음
'''
visited = [False] * (N+1)
def bfs(graph, start):
    q = deque()
    
    q.append(start)
    while q:
        now = q.popleft()
        print(now, end=" ")
        visited[now] = True
        
        for node in graph[now]:
            if visited[node] == False:
                q.append(node)
                visited[node] = True
                
bfs(graph, V)
print()