import sys
sys.setrecursionlimit(10**9)
from collections import Counter

def find_parent(parent, x):
    if parent[x][0] != x:
        parent[x][0] = find_parent(parent, parent[x][0])
    return parent[x][0]


def union(x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    
    if x < y:
        parent[y] = [x, parent[y][1]]
        parent[x] = [x, parent[x][1] + parent[y][1]]
    else: 
        parent[x] = [y, parent[x][1]]
        parent[y] = [y, parent[x][1] + parent[y][1]]
    
    
T = int(input())
for _ in range(T):
    N = int(input())
    name = dict()
    parent = []    # parent에는 [부모의 idx, 네트워크 사람 수]가 저장된다.
    
    for _ in range(N):
        a, b = sys.stdin.readline().strip().split()
        if a not in name:
            name[a] = len(name)
            parent.append([len(parent), 1])
        if b not in name:
            name[b] = len(name)
            parent.append([len(parent), 1])
            

        if find_parent(parent, name[a]) != find_parent(parent, name[b]):
            union(name[a], name[b])
    
        
        result = max(parent[parent[name[a]][0]][1], parent[parent[name[b]][0]][1])
        print(result)
        
''' [review]
N이 최대 10만이라서 매 반복마다 count 또는 중첩 반복으로
네트워크에 존재하는 사람 수를 세려면 시간 초과 뜰 것 같아서
union 과정에서 parent 정보에 사람 수 까지 저장해줘야겠다.

=> parent에 저장안하고 num변수 선언해서 사용하면 시간복잡도나 구현에 더 용이함.
'''
