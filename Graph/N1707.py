import sys
from collections import deque


def bfs(graph, group, i):
    group[i] = 'A'
    q = deque([i])
    
    while q:
        u = q.popleft()
        
        for v in graph[u]:
            if group[v] == None:
                group[v] = 'A' if group[u]=='B' else 'B'
                q.append(v)
            
            else:
                if group[u] == group[v]:
                    return 1    # NO
    
    return 0    # YES

T = int(sys.stdin.readline().strip())
for _ in range(T):
    V, E = map(int, sys.stdin.readline().strip().split())
    graph = [[] for _ in range(V+1)]
    group = [None] * (V+1)
    
    for _ in range(E):
        u, v = map(int, sys.stdin.readline().strip().split())
        graph[u].append(v)
        graph[v].append(u)
    
    MAX = 0
    for i in range(1, V+1):
        print(group)
        if group[i] == None:
            result = max(MAX, bfs(graph, group, i))
    
    if result == 1:
        print("NO")
    else: print("YES")

''' [review]
그래프가 이어져있지 않을 경우도 생각해야함
ex. 1번 노드에서 V노드를 가는 경로가 없는 경우
'''