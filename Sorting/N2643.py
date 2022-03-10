import sys
from collections import deque

N = int(sys.stdin.readline().strip())
array = [tuple(map(int, sys.stdin.readline().strip().split()))
        for _ in range(N)]

# 그래프 생성 big -> small
graph = [[] for _ in range(N)]
for idx_big, big in enumerate(array):
    for idx_small, small in enumerate(array):    
        if (small[0] <= big[0] and small[1] <= big[1]) or (small[1] <= big[0] and small[0] <= big[1]):
                if idx_big != idx_small:
                    graph[idx_big].append(idx_small)
# print(graph)
# bfs로 가장 깊은 depth구하기
max_depth = 0
def bfs(start):
    global max_depth
    q = deque([(start, 1)])
    
    while q:
        u, depth = q.popleft()
        for v in graph[u]:
            # print(u, v, depth)
            q.append((v, depth+1))
            if max_depth < depth+1:
                max_depth = depth + 1

for i in range(N):
    bfs(i)
    
print(max_depth)

'''
[[],     [0],    [0, 1], [0, 1, 4, 5, 6], [0, 1, 6], [0, 1, 6],  [0, 1]]
(1, 2), (8, 7), (20, 10), (20, 20),       (15, 12),   (12, 14),  (11, 12)
0         1        2          3             4              5        6
'''