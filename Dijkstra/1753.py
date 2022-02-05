import sys
import heapq

V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V+1)]
distance = [10**9] * (V+1)

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().strip().split())
#    for i in range(len(graph[u])):    # 간선이 여러개인 경우 최단 간선만 저장
#        if graph[u][i][0] == v and graph[u][i][1] >= w:
#            del graph[u][i]

    graph[u].append((v, w))    # 각 정점 노드에 (반대 노드, 거리)가 저장됨

''' [dijkstra]
1. 자기 자신과의 거리는 0
2. 시작 점을 힙에 넣고
3. 힙에서 가장 최소 거리의 노드를 빼내어,
4. 해당 노드의 인접노드 중 방문하지 않은 노드에 대해 거리를 갱신
5. 반복
'''
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

dijkstra(start)
for i in range(1, V+1):
    if distance[i] == 10**9:
        print("INF")
    else:
        print(distance[i])

''' [review]
1. 나는 문제에서 "서로 다른 두 정점 사이에 여러 개의 간선이 존재 가능"이라길래
두 정점 사이에 간선이 여러개인 경우, 최단 간선만 저장하는 것으로 처리했다. => 런타임 발생
if distance(u_num) < dis 에서 방문 여부를 확인할 때,
이미 다른 간선에 의해 distance가 조정되는 경우 dis보다 작은 것으로 처리되어
방문 여부 True처리 될 것을 염려했다.
=> 모든 간선을 저장해도 문제 없는 이유는 무엇인가?
=> 최단 거리는 힙에서 빼는 경우에 확정된다.
최단 거리에 해당하는 간선을 빼기 전까지
모든 간선들이 힙에 추가된다. 그 이후에 그 많은 간선들 중에 최소를 꺼내는 것이다.
" 최단 간선을 제외한 나머지 간선은 나중에 나와서 제거될 뿐이다 "

2. if distance[u_num] < dis 가 방문했음을 의미하는 이유
: 여기서 dis는 단순히 v에서 u까지의 w를 의미하지 않음.
힙에 저장할 때 distance(v)+w인 cost를 저장하기 때문.
인접 정점의 distance가 cost보다 작으면 이미 다른 정점에 의해
최단 거리 distance가 확정되었음을 의미한다.
++ 힙에서 꺼낼 때 확인해야 한다.
==> 힙에서 꺼낼 때 최단 거리가 확정되는 구조임.
"힙에서 빼는 행위 == 최단거리 확정"으로 기억하자.
'''