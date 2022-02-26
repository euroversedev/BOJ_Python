import sys
sys.setrecursionlimit(10**9)


N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split()) 
    graph[a].append(b)
    graph[b].append(a)
    
max_ = 0    
def dfs(visited, i, deep):
    global max_
    if deep > max_: max_ = deep
    visited[i] = True

    for friend in graph[i]:
        if visited[friend] == False:
            visited[friend] = True
            dfs(visited, friend, deep+1)

              
    

for i in range(N):
    visited = [False] * N
    dfs(visited, i, 1)

if max_ > 4: print(1)
else: print(0)