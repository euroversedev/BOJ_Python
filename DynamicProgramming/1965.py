import sys

N = int(input())
array = list(map(int, sys.stdin.readline().strip().split()))
dp = [1] * N
for i in range(N):
    max_dp = 0
    for j in range(i):
        if array[i] > array[j] and max_dp < dp[j]:
            max_dp = dp[j]
            
    dp[i] += max_dp
print(max(dp))