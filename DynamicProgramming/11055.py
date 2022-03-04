import sys

N = int(input())
array = list(map(int, sys.stdin.readline().strip().split()))

dp = [0] * (N)
dp = array[:]
for i in range(N):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], array[i]+dp[j])

print(max(dp))