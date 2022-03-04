import sys

C, N = map(int, sys.stdin.readline().strip().split())
array = [tuple(map(int, sys.stdin.readline().strip().split()))
        for _ in range(N)]

# 사람 수를 나타내는 DP
dp = [10**9] * (C+1)

dp[0] = 0
for i in range(C+1):
    for price, person in array:
        for j in range(i+1, i+person+1):
            if j < C+1:
                dp[j] = min(dp[j], dp[i] + price)

print(dp[-1])
        