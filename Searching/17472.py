import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split()))
        for _ in range(N)]
graph = [[] for _ in range(8)] # 섬 갯수 2~6개

def bfs(y, x, num):
    board[y][x] = num
    q = deque([(y, x)])
    
    while q:
        y, x = q.popleft()
        
        for dy, dx in [(1,0),(0,1),(-1,0),(0,-1)]:
            if 0<=y+dy<N and 0<=x+dx<M and board[y+dy][x+dx] == 1:
                board[y+dy][x+dx] = num
                q.append((y+dy, x+dx))

# 섬에 이름 지어주기
num = 2
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            bfs(i, j, num)    # 이름이 num인 섬
            num += 1



# 가능한 가로 다리(간선) 구하기
for y in range(N):
    u = 0
    cnt = 0    #거리
    
    for x in range(M):
        if 0<=x-1 and board[y][x-1] != 0 and board[y][x] == 0:
            u = board[y][x-1]
        
        if 0<=x-1 and board[y][x-1] == 0 and board[y][x] != 0 and u!= 0:
            if cnt > 1:
                graph[u].append((board[y][x], cnt))
                graph[board[y][x]].append((u,cnt))
            u = 0
            cnt = 0
            continue
            
        if u != 0 and board[y][x] == 0:
            cnt += 1
            continue
# for y in range(N):
#     u = 0
#     cnt = 0
    
#     for x in range(M):
#         if board[y][x] == 0:
#             cnt += 1
#             continue
        
#         if u == 0 and board[y][x] != 0:
#             u = board[y][x]
#             continue
            
#         if u != 0 and board[y][x] != 0 and u != board[y][x]:
#             if cnt > 1:
#                 graph[u].append((board[y][x], cnt))
#             u = 0
#             cnt =0
            
# 가능한 세로 다리 구하기
for x in range(M):
    u = 0
    cnt = 0    #거리
    
    for y in range(N):
        if 0<=y-1 and board[y-1][x] != 0 and board[y][x] == 0:
            u = board[y-1][x]
        
        if 0<=y-1 and board[y-1][x] == 0 and board[y][x] != 0 and u!= 0:
            if cnt > 1:
                graph[u].append((board[y][x], cnt))
                graph[board[y][x]].append((u,cnt))
            u = 0
            cnt = 0
            continue
            
        if u != 0 and board[y][x] == 0:
            cnt += 1
            continue
        
        
# 크루스컬
parent = [i for i in range(8)]

def find_parent(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find_parent(parent[x])
        return parent[x]
    
def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    
    if a < b: parent[b] = a
    else: parent[a] = b
        

list_ = []
for i in range(8):
    for v, w in graph[i]:
        list_.append((w, i, v))

result = 0
for bridge in sorted(list_):
    w, u, v = bridge
    
    if find_parent(u) == find_parent(v):
        continue
        
    else:
        union_parent(u, v)
        result += w

if result == 0 :
    print(-1)
    exit()
print(result)








''' review
1. BFS로 섬마다 이름 지어줄거임 (2, 3, 4...)
2. 모든 행과 셀을 돌면서 가능한 다리를 모두 탐색 (간선) => 그래프화
3. 크루스컬로 MST 만들기
'''