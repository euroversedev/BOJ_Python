import sys
import heapq

N, M = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(N)]

light = list(map(int, sys.stdin.readline().strip().split()))

for _ in range(M):
    a, b, w = map(int, sys.stdin.readline().strip().split())
    
    # 시야가 있는 곳은 아예 간선도 저장하지 않을 것임..
    if light[a] and a != N-1: continue
    if light[b] and b != N-1: continue
    
    # 양방향 그래프 생성
    graph[a].append((b, w))
    graph[b].append((a, w))

# dijkstra로 0에서 N-1까지의 최단 경로 구하기
dis = [10**9] * N
def dijkstra(start):
    dis[start] = 0
    
    h = []
    heapq.heappush(h, (0, start))    # 노드 번호와 거리
    
    while h:
        distance, u = heapq.heappop(h)
        
        if distance > dis[u]:
            continue
        
        # 주변 노드들에 대한 거리를 갱신
        for v, w in graph[u]:
            cost = distance + w 
            
            if cost < dis[v]:
                dis[v] = cost
                heapq.heappush(h, (cost, v))

dijkstra(0)
print(dis[N-1] if dis[N-1] != 10**9 else -1)