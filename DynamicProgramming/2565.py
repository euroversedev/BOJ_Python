import sys

N = int(input())
array = [tuple(map(int, sys.stdin.readline().strip().split()))
        for _ in range(N)]


A, B = zip(*sorted(array))

dp = [0] * N

for i in range(N):
    max_dp = 0
    for j in range(i):
        if B[j] < B[i] and max_dp < dp[j]:
            max_dp = dp[j]
    dp[i] = max_dp + 1

print(N-max(dp))