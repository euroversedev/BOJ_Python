import sys
import heapq

N, M, X = map(int, sys.stdin.readline().strip().split())
# X에서 나머지 노드로 가는 거리를 구하는 그래프
graph_fromX = [[] for _ in range(N+1)]
dis_fromX = [10**9] * (N+1)

# 나머지 노드에서 X로 가는 거리를 구하는 그래프
graph_toX = [[] for _ in range(N+1)]
dis_toX = [10**9] * (N+1)


for _ in range(M):
    a, b, w = map(int, sys.stdin.readline().strip().split())
    graph_fromX[a].append((b, w))
    graph_toX[b].append((a, w))


def dijkstra(graph, dis_list, start):
    dis_list[start] = 0
    h = []
    heapq.heappush(h, (0, start))
    
    while h:
        dis, u = heapq.heappop(h)
        
        if dis_list[u] < dis:
            continue
            
        for v, w in graph[u]:
            cost = dis + w
            
            if cost < dis_list[v]:
                dis_list[v] = cost
                heapq.heappush(h, (cost, v))

    
dijkstra(graph_fromX, dis_fromX, X)
dijkstra(graph_toX, dis_toX, X)


max_ = 0
for i in range(1, N+1):
    tmp = dis_toX[i] + dis_fromX[i]
    if max_ < tmp: max_ = tmp

print(max_)