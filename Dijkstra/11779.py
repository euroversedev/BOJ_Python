import sys
import heapq

N = int(input())
E = int(input())

graph = [[] for _ in range(N+1)]

# 지나쳐온 노드를 저장하는 dp
dp = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, w = map(int, sys.stdin.readline().strip().split())
    graph[a].append((b, w))

dis_list = [10**9] * (N+1)
def dijkstra(start, end):
    dis_list[start] = 0
    dp[start].append(start)
    
    h = []
    heapq.heappush(h, (0, start))    # 거리가 0
    
    while h:
        dis, u = heapq.heappop(h)
        
        if dis_list[u] < dis:    # 이미 방문한 노드
            continue   
        
        for v, w in graph[u]:
            cost = dis + w
            
            if cost < dis_list[v]:
                dis_list[v] = cost
                heapq.heappush(h, (cost, v))
                
                dp[v] = dp[u]+[v]
                    
        
x, y = map(int, sys.stdin.readline().strip().split())

dijkstra(x, y)

print(dis_list[y])
print(len(dp[y]))
print(*dp[y], sep=' ')
