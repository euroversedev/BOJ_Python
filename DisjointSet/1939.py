from collections import deque
import sys
sys.setrecursionlimit(10**9)

N, M = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
# 시간 복잡도를 줄이기 위해 (선형탐색 피하기) 인접 정점 정보를 따로 저장
adjacent = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    
    # 두 섬 사이의 중량이 최대인 다리만 저장함
    if c > graph[a][b]:
        graph[a][b], graph[b][a] = c, c
    
    for x, y in [(a, b), (b, a)]:
        if x not in adjacent[y]:
            adjacent[y].append(x)

start, end = map(int, input().split())

# max_weights[i]는 start에서 i까지 갈 수 있는 최대 중량을 저장한다.
max_weights = [0] * (N+1)

visited = [False] * (N+1) 
def bfs(start, end):
    visited[start] = True
    q = deque([start])
    max_weights[start] = 10**9
    
    while q:
        u = q.popleft()
        visited[u] = True
        
        for v in adjacent[u]:
            if visited[v] == False:    # 방문하지 않은 섬에 대해
                max_weights[v] = max(max_weights[v], min(max_weights[u], graph[u][v]))
                q.append(v)

bfs(start, end)

print(max_weights[end])
    
''' [review]
첫번째 접근:
bfs로 start에서 시작해서 end로 끝나는 모든 경우에 대해서
최대 중량을 갱신한다. => max_weights[end]를 출력한다.
=> 메모리 초과가 나옴
★ (질문글에 대한 답변 피셜)
정점의 수가 많고 간선의 수가 V^2에 한참 못미치는 문제에서는
인접 행렬이 아니라 인접 리스트로 해결하는 것이 바람직하다.
=> 1939_2.py
'''
    
    
    
    