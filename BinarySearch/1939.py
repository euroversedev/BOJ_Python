import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, w = map(int, sys.stdin.readline().strip().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

A, B = map(int, sys.stdin.readline().strip().split())

# weight 무게로 A섬에서 B섬으로 이동 가능한지 탐색
def bfs(weight):
    visited = [False] * (N+1)
    visited[A] = True
    q = deque([A])
    
    while q:
        u = q.popleft()
        
        for v, w in graph[u]:
            if w >= weight and visited[v]==False:
                visited[v] = True
                q.append(v)
    
    return visited[B]
      
result = 0
start, end = 0, 10**9
while start <= end:
    mid = (start+end)//2
    
    # 이동 가능 여부 체크
    flag = bfs(mid)
    
    # 중량 mid가 A섬에서 B섬으로 이동 가능한 경우 => 더 무거운 무게 시도
    if flag:
        result = mid
        start = mid +1
    
    else:
        end = mid -1

print(result)
''' review
이진 탐색으로 중량 조절하면서,
각 반복마다 BFS로 이동 가능 여부 체크
'''