import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[b].append(a)
    
# def dfs(graph, visited, u):
#     visited[u] = True
    
#     result = 1
#     for v in graph[u]:
#         if visited[v] == False:
#             result += dfs(graph, visited, v)
    
#     return result

def bfs(start):
    visited = [False] * (N+1)
    visited[start] = True
    q = deque([start])
    cnt = 1
    
    while q:
        u = q.popleft()
        
        for v in graph[u]:
            if visited[v] == False:
                visited[v] = True
                q.append(v)
                cnt += 1
    return cnt

max_ = 0
ans = []
for i in range(1, N+1):
    if len(graph[i]) > 0:
        result = bfs(i)

        if result > max_:
            max_ = result
            ans = [i]
            continue
        if result == max_:
            ans.append(i)
        
        #dp[i] = dfs(graph, visited, i)
        
print(*ans)
#max_ = max(dp)
#print(*list(i for i in range(1, N+1) if dp[i] == max_))

''' review
dfs 시간 복잡도


dfs로 각 컴퓨터가 해킹할 수 있는 컴퓨터의 갯수를 가져올 것임.
dp에 저장해서 한번 구했던 컴퓨터는 다시 구하지 않음.
dp에 저장된 가장 큰값을 가진 컴퓨터들을 출력
=> 이미 구한 dp를 이용해서 구현할 수 없음..
=> 싸이클이 존재하는 경우를 고려해야하기 때문.
'''