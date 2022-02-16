N = int(input())
array = [0] + [int(input()) for _ in range(N)]
dp = [0] * (N+1)

dp[N] = array[N]
dp[N-1] = array[N] + array[N-1]
dp[N-2] = max(array[N-2]+array[N], array[N-2]+array[N-1])

for i in range(N-3, 0, -1):
    dp[i] = array[i] + max(dp[i+2], array[i+1]+dp[i+3])

print(dp[1])


