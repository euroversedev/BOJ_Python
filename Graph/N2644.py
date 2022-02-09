import sys

N = int(input())
a, b = map(int, input().split())
E = int(input())
graph = [None] * (N+1)
for _ in range(E):
    parent, child = map(int, sys.stdin.readline().strip().split())
    graph[child] = parent    # 자식이 부모를 가리킴

def dfs(a, b):
    if a == b:
        return 1
    
    if graph[a] == None and graph[b] == None:
        return -1
    
    