import sys

N = int(input())
dp = [0] * N

max_ = 0
for i in range(N):
    T, P = map(int, sys.stdin.readline().strip().split())
    
    if i + T - 1 < N:
        if dp[i+T-1] < max_+P : dp[i+T-1]=max_+P
    
    if max_ < dp[i]: max_ = dp[i]
    
print(max(dp))