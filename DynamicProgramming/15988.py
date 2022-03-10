import sys

dp = [0, 1, 2, 4] + [0]*(10**6)
for i in range(4, 10**6+1):
    dp[i] = (dp[i-1]+dp[i-2]+dp[i-3]) % 1000000009

T = int(input())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    print(dp[N])
