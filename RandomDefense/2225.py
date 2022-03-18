import sys
sys.setrecursionlimit(10**9)

N, K = map(int, sys.stdin.readline().strip().split())

dp = dict()
# dfs
def dfs(prefix_sum, depth):
    if prefix_sum == N and depth == K:
        return 1
    
    if (prefix_sum, depth) in dp:
        return dp[(prefix_sum, depth)]
    dp[(prefix_sum, depth)] = sum([dfs(prefix_sum + x, depth+1) for x in range(N+1) if prefix_sum+x<=N and depth+1<=K])%(10**9)

    return dp[(prefix_sum, depth)]
print(dfs(0, 0))