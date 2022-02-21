import sys

N, K = map(int, sys.stdin.readline().strip().split())
array = sorted([list(map(int, sys.stdin.readline().strip().split()))
                for _ in range(N)], key = lambda x:(-x[0], x[1]))

dp = [0] * (K+1)
for w, v in array:
    for j in range(K, -1, -1):
        if j + w < K+1 and (dp[j+w] < dp[j] + v):
            dp[j+w] = dp[j] + v

print(max(dp))
