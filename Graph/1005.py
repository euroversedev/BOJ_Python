import sys
from collections import deque

def topology(graph, Indegree, delay, target, sum_delay):
    q = deque()
    for i in range(1, N+1):
        if Indegree[i] == 0:
            q.append(i)
            sum_delay[i] = delay[i]
            
    while q:
        start= q.popleft()
        if start == target:
            return sum_delay[start]    #@@@@@@@???
        
        for end in graph[start]:
            Indegree[end] -= 1
            sum_delay[end] = max(sum_delay[end], sum_delay[start]+delay[end])
            if Indegree[end] == 0:
                q.append(end)
        
T = int(sys.stdin.readline().strip())
for _ in range(T):
    N, K = map(int, sys.stdin.readline().strip().split())
    graph = [[] for _ in range(N+1)]
    Indegree = [0] * (N+1)
    delay = [0] + list(map(int, sys.stdin.readline().strip().split()))
    sum_delay = [0] * (N+1)
    for _ in range(K):
        a, b = map(int, sys.stdin.readline().strip().split())
        graph[a].append(b)
        Indegree[b] += 1
    target = int(sys.stdin.readline().strip())
    
    print(topology(graph, Indegree, delay, target, sum_delay))
    