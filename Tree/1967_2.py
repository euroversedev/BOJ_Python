import sys

class Node:
    def __init__(self, data, w):
        self.data = data
        self.child = []
        self.dp = (0,0)    # (자식 중 큰 것, 자식의 합)
        self.w = w
        
tree = dict()
tree[1] = Node(1, 0)
N = int(sys.stdin.readline().strip())
for _ in range(N-1):
    p, c, w = map(int, sys.stdin.readline().strip().split())
    # 부모와의 거리가 자식 노드에 저장됨
    tree[c] = Node(c, w)
    tree[p].child.append(c)

def solution(p):
    max_ = 0
    ws = []
    for children in tree[p].child:
        max_ = max(max_, tree[children].dp[0] + tree[children].w)
        ws.append(tree[children].dp[0] + tree[children].w)
    
    sum_ = 0
    if len(ws) > 0:
        ws.sort()
        sum_ = ws[-1]
        if len(ws) > 1:
            sum_ += ws[-2]
            
    # idx가 None을 반환 받은 경우도 고려해야함
    
    tree[p].dp = (max_, sum_)

result = 0
for i in range(N, 0, -1):
    solution(i)
    result = max(result, tree[i].dp[1])

print(result)

''' [review]
트리라고는 하지만
Node 클래스 만들지않고 기존에 그래프 구현하듯이
인접 정점 리스트 만들어서 구현할 수도 있음.
=> dfs로 푸는게 가장 정석에 가까운듯?
각 정점마다 최대 지름을 구할 수 있다는 생각

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def dfs(x):
    m = 0
    for i, j in s[x]:
        d[x].append(j + dfs(i))
        m = max(m, d[x][-1])
    return m

n = int(input())
s = [[] for _ in range(n+1)]
d = [[0] for _ in range(n+1)]
for _ in range(n-1):
    a, b, e = map(int, input().split())
    s[a].append((b, e))
dfs(1)

r = 0
for i in d:
    i.sort(reverse=True)
    r = max(r, sum(i[:2]))
print(r)

'''
