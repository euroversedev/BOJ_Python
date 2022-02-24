import sys
import heapq

N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]
edges = [10**9] * (E+1)
for i in range(E):
    a, b, w = map(int, sys.stdin.readline().strip().split())
    graph[a].append((b, w))
    graph[b].append((a, w))
    edges[i] = w

''' kruskal Algorithm
MST 구하기는 간선을 기준으로 작동함. 배낭에 집어넣기
'''
def kruskal():
    dis = [10**9] * (N+1)
    
    
    
    
    
print(kruskal())