import sys
from collections import deque

N, K = map(int, input().split())
maxNK = max(N+1, 2*K)
visited = [False] * maxNK

def bfs(x):
    visited[x] = True
    q = deque([(x, 0)])

    while q:
        num, depth = q.popleft()
        
        if num == K:
            return depth
        
        for dq in [num-1, num+1, num*2]:
            if 0<=dq<maxNK and visited[dq]==False:
                visited[dq] = True
                q.append((dq, depth+1))
        
result = bfs(N)
print(result)


''' [review]
위 코드에서 N이 무조건 K를 넘을 수 없다는 조건이 없으므로
50 99를 입력하면 50->100->99로 답이 2가되어야한다.
N이 K를 넘어도 되도록 코딩해보자


원래 시도했던 코드

import sys
sys.setrecursionlimit(10**9)

N, K = map(int, input().split())

def dfs(X, depth):
    if X == K:    # 동생 찾은 경우
        return depth
    
    elif 0 <= X < K:    # 수빈이보다 동생이 오른쪽에 있는 경우
        a = dfs(X+1, depth+1)
        b = dfs(2*X, depth+1)
        c = dfs(X-1, depth+1)
        return min(a, b, c)
    
    elif X > K:    # 수빈이가 동생보다 오른쪽에 있는 경우 -만 가능
        d = dfs(X-1, depth+1)
        return d

result = dfs(N, 0)
print(result)
'''