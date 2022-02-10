import sys

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    # v가 u를 신뢰한다 = u가 v를 감염시킬 수 있다.
    v, u = map(int, sys.stdin.readline().strip().split())
    graph[u].append(v)   

visited = [-1] * (N+1)

def dfs(u):
    if len(graph[u]) == 0: #감염시킬 PC가 없는 경우
        visited[u] = 0
        return 1
        
    if visited[u] != -1:
        return visited[u] + 1
    
    else:
        visited[u] = 0
        for v in graph[u]:
            visited[u] += dfs(v)
    
    return visited[u] + 1
        
        
for i in range(1, N):
    if visited[i] == -1:
        dfs(i)

sorted_visited = sorted(enumerate(visited), key = lambda x: (x[1], x[0]))
a = [sorted_visited[i][0] for i in range(1, N+1) if sorted_visited[i][1] == sorted_visited[-1][1]]
print(visited)
print(*a)

''' [review]
1520과 매우 유사 

반례: A가 (B와 C)에 의해 결정되고 B가 C에 의해 결정되면
      A는 C를 중복해서 반영하게 됨.
5 4
3 2
4 3
5 4
4 2
'''

