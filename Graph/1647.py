import sys
''' 크루스컬 알고리즘
: Minimum Spanning Tree (최소신장트리)를 구하는 알고리즘

Union Find를 이용해서 사이클이 발생하지 않도록,
최소 간선들을 배낭에 추가해 나간다. => 최소 간선
'''

N, M = map(int, input().split())
parent = [i for i in range(N+1)]
array = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]
array = sorted(array, key= lambda x: (x[2], x[0], x[1]))

def find_parent(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find_parent(parent[x])
        return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

        
result = []
for a, b, w in array:
    
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result.append(w)
        
    else:
        continue
        
print(sum(sorted(result)[:-1]))
        