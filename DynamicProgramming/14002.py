import sys

N = int(input())
array = list(map(int, sys.stdin.readline().strip().split()))
dp = [0] * (N)

for i in range(N):
    max_dp = 0
    for j in range(i):
        if array[i] > array[j] and dp[j] > max_dp:
            max_dp = dp[j]
    dp[i] = max_dp + 1

max_dp = max(dp)
print(max_dp)
    
LIS = []
max_idx = dp.index(max(dp))
max_num = 10**9
for idx in range(max_idx, -1, -1):
    if max_dp == dp[idx] and max_num > array[idx]:
        LIS.append(array[idx])
        max_dp -= 1
        max_num = array[idx]
print(*LIS[::-1])
    