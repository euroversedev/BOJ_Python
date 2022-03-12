import sys
from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().strip().split())
    graph = [[] for _ in range(N+1)]
    
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().strip().split())
        graph[a].append(b)
        graph[b].append(a)
        
    # bfs
    visited = [False] * (N+1)
    visited[1] = True
    q = deque([1])
    
    cnt = 0
    while q:
        u = q.popleft()
        
        for v in graph[u]:
            if visited[v] == False:
                visited[v] = True
                q.append(v)
                cnt += 1
    
    print(cnt)


'''
bfs dfs union&find 등으로 풀 수 있음
'''