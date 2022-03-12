import sys

N = int(input())
array = list(map(int, sys.stdin.readline().strip().split()))

dp = [10**9] * (N)
dp[0] = 0
for i in range(N):
    for j in range(i+1, i+1+array[i]):
        if j >= N: continue
        dp[j] = min(dp[j], dp[i]+1)
        
print(dp[-1] if dp[-1] < 10**9 else -1)
