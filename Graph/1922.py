import sys


N = int(input())
parent = [i for i in range(N+1)]

M = int(input())
edges = []
for _ in range(M):
    a, b, w = map(int, sys.stdin.readline().strip().split())
    edges.append((w, a, b))
    
    
def find_parent(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find_parent(parent[x])
        return parent[x]
    
def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)
    
    if x < y:
        parent[y] = x
    else: parent[x] = y
    
def kruskal():
    edges.sort()
    
    sum_w = 0
    for w, start, end in edges:
        if find_parent(start) != find_parent(end):
            union_parent(start, end)
            sum_w += w    
        
    return sum_w

print(kruskal())
    
