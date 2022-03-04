import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(i):
    visited = [False]*N
    visited[i] = True
    q = deque([(i, 1)])
    
    while q:
        u, depth = q.popleft()
        if depth >= 4:
            return True
        
        for v in graph[u]:
            if visited[v] == False:
                visited[v] = True
                q.append((v, depth+1))
    return False

for i in range(N):
    if bfs(i):
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
'''