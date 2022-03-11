from collections import deque

N = int(input())

dp = deque([0,3,7])
for i in range(3, N+1):
    dp.append((dp[-1]*2+dp[-2])%9901)
    dp.popleft()

if N > 2:
    print(dp[-1])
else:
    print(dp[N])