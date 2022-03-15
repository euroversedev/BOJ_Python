import sys

N = int(input())
array = list(map(int, sys.stdin.readline().strip().split()))
K = int(input())

interval_sum = []
sum_ = sum(array[:K])
start = 0
end = K-1
for i in range(N-K+1):
    interval_sum.append(sum_)
    try:
        sum_ += array[end+1] - array[start]
        start, end = start+1, end+1
    except:
        break
    
dp = [[0] * len(interval_sum) for _ in range(4)]
for i in range(K):
    dp[1][i] = interval_sum[i]
dp[1][K] = max(dp[1][0], interval_sum[K])
dp[2][K] = interval_sum[0] + interval_sum[K]

for x in range(K+1, len(interval_sum)):
    start = x-2*K+1 if x-2*K+1 >= 0 else 0
    dp[1][x] = max(dp[1][start:x-K+1] + [interval_sum[x]])
    dp[2][x] = max([ max(dp[1][start:x-K+1]) + interval_sum[x] ]+ dp[2][start:x-K+1])
    dp[3][x] = max([ max(dp[2][start:x-K+1]) + interval_sum[x] ]+ dp[3][start:x-K+1])

print(max(dp[3]))