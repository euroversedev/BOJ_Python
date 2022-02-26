import sys
sys.setrecursionlimit(10**9)

def dfs(graph, visited, group, start):
    visited[start] = True
    
    flag = True
    for end in graph[start]:
        if group[start] == group[end]:
            return False
        
        if group[end] == 0:
            if group[start] == 1:
                group[end] = 2
            elif group[start] == 2:
                group[end] = 1
        
        if visited[end] == False:
            flag = dfs(graph, visited, group, end)
    return flag
    

T = int(input())
for _ in range(T):
    V, E = map(int, sys.stdin.readline().strip().split())
    graph = [[] for _ in range(V+1)]
    visited = [False] * (V+1)
    group = [0] * (V+1)
    for _ in range(E):
        a, b = map(int, sys.stdin.readline().strip().split())
        graph[a].append(b)
        graph[b].append(a)

    result = True
    for i in range(1, V+1):
        if visited[i] == False:
            group[i] = 1
            if dfs(graph, visited, group, i) == False:
                result = False

    if result: print("YES")
    else: print("NO")