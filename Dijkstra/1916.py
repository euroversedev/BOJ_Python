import sys
import heapq

V = int(input())
E = int(input())
graph = [[] for _ in range(V+1)]
distance = [10**9] * (V+1)

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().strip().split())

    graph[u].append((v, w))    # 각 정점 노드에 (반대 노드, 거리)가 저장됨

def dijkstra(start):
    distance[start] = 0
    
    h = []    # 힙은 리스트로 만든다
    heapq.heappush(h, (distance[start], start))    # 튜플형태로 거리와 같이 넣어줌
    
    while h:
        dis, u_num = heapq.heappop(h)

        if distance[u_num] < dis:    # 방문했음을 의미함, 합에서 꺼낼때 확인해야 함.
            continue    
        
        for v_num, w in graph[u_num]:
            cost = dis + w
        
            if cost < distance[v_num]:
                distance[v_num] = cost
                heapq.heappush(h, (cost, v_num))

start, end = map(int, input().split())
dijkstra(start)
print(distance[end])
