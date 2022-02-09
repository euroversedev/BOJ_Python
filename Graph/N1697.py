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