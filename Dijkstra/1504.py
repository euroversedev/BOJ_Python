import sys
import heapq

N, E = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, w = map(int, sys.stdin.readline().strip().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

''' 다익스트라 최단경로 알고리즘
1. 자기 자신과의 거리는 0으로 하고 힙에 넣음
반 2. 힙에서 꺼내어 인접 정점들의 최단거리를 갱신
복 3..
'''
def dijkstra(start, end):
    dis_list = [10**9] * (N+1)
    dis_list[start] = 0
    
    h = []
    heapq.heappush(h, (0, start))    # 거리가 0
    
    while h:
        dis, u = heapq.heappop(h)
        
        if dis_list[u] < dis:    # 이미 방문한 노드
            continue   
        
        for v, w in graph[u]:
            cost = dis + w
            
            # if dis_list[v] < cost:    # 이미 방문한 노드
            #     continue            ## 여기는 cost인가 dis인가 @@@@@@@
                
            if cost < dis_list[v]:
                dis_list[v] = cost
                heapq.heappush(h, (cost, v))
    
    return dis_list[end]
    
    
    
x, y = map(int, sys.stdin.readline().strip().split())

case1 = dijkstra(1, x) + dijkstra(x, y) + dijkstra(y, N)
case2 = dijkstra(1, y) + dijkstra(y, x) + dijkstra(x, N)

result = case1 if case1 < case2 else case2
if result < 10**9: print(result)
else: print(-1)