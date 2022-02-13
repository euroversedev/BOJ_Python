from collections import deque
import sys
sys.setrecursionlimit(10**9)

N, M = map(int, input().split())
graph = [dict() for _ in range(N+1)]
list_c = []

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    list_c.append(c)
    
    # 두 섬 사이의 중량이 최대인 다리만 저장함
    if (b not in graph[a]) or (c > graph[a][b]):
        graph[a][b], graph[b][a] = c, c

list_c.sort()
result = binary_search(1, list_c[-1])
        
    
    
start, end = map(int, input().split())

# max_weights[i]는 start에서 i까지 갈 수 있는 최대 중량을 저장한다.
max_weights = [0] * (N+1)

visited = [False] * (N+1) 
def bfs(start, end):
    visited[start] = True
    q = deque([start])
    max_weights[start] = 10**9
    
    while q:
        u = q.popleft()
        visited[u] = True
        
        for v, w in graph[u].items():
            if visited[v] == False:    # 방문하지 않은 섬에 대해
                max_weights[v] = max(max_weights[v], min(max_weights[u], graph[u][v]))
                q.append(v)
        
bfs(start, end)

print(max_weights[end])
    
''' [review]
나도 BFS로 풀었고 질문 게시판에서도 대부분 BFS로 풀었다고, 아래와 같은 TC에서 틀림. 
생각해보니.. BFS로 하면 하나의 노드에 대해 여러번 갱신이 안되는거 아닌가?
한 번 방문하고 max_weights을 갱신하고 나면 다시는 방문 못하잖아
'''
    
    
    
    