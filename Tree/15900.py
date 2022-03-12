import sys
from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

# bfs
visited = [False] * (N+1)
visited[1] = True
q = deque([(1, 0)]) # 노드 번호, depth

sum_leaf_depth = 0
while q:
    u, depth = q.popleft()
    
    # 자식 노드 방문 여부 flag
    flag = False
    for v in graph[u]:
        if visited[v] == False:
            visited[v] = True
            q.append((v, depth+1))
            flag = True
            
    # 자식이 없으면, leaf노드
    if flag == False:
        sum_leaf_depth += depth

print("Yes" if sum_leaf_depth%2==1 else "No")



''' review
bfs로 루트부터 리프까지의 거리 "합"을 계산
합이 짝수 => 못이김
'''