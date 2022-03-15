import sys
from collections import deque

N = int(input())

graph = [[] for _ in range(N+1)]
w  = [0] * (N+1) # 각 건물을 짓는데 걸리는 시간
indegree = [0] * (N+1) # 차수
answer = [0] * (N+1)

# 노드 및 간선 생성
for v in range(1, N+1):
    array = list(map(int, sys.stdin.readline().strip().split()))

    w[v] = array[0]
    for u in array[1:]:
        if u == -1: break
        
        graph[u].append(v)
        indegree[v] += 1
        
# 위상 정렬 => 차수가 0 인것들에 대해 수행
pre_w = [0] * (N+1)
q = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    u= q.popleft()
    
    answer[u] = pre_w[u] + w[u]
    
    for v in graph[u]:
        indegree[v] -= 1
        
        if pre_w[v] < answer[u]:
            pre_w[v] = answer[u]
        
        if indegree[v] == 0:
            q.append(v)

print(*[answer[i] for i in range(1, N+1)], sep='\n')
          
''' 위상 정렬 문제 '''