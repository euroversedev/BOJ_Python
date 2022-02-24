import sys
def floyd_warshall(n):
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

n = int(input())
m = int(input())
graph = [[int(1e9)] * (n+1) for _ in range(n+1)]

# 출발 노드와 도착 노드가 같은 경우, 최단거리 = 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b: graph[a][b] = 0

# 간선 입력
for _ in range(m):
    a, b, w = map(int, sys.stdin.readline().strip().split())
    graph[a][b] = min(graph[a][b], w)

# 출력
floyd_warshall(n)
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == int(1e9): print(0, end=" ")
        else: print(graph[a][b], end=" ")
    print()
    