import sys

N = int(input())
dp = [10**9] * (N+1)

dp[1] = 0
for i in range(2, N+1):
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
        
    dp[i] = min(dp[i], dp[i-1]+1)

print(dp[N])

k = dp[N]-1
result = [N]
for j in range(N-1, 0, -1):
    if dp[j] == k:
        if (j == (result[-1] // 3) and result[-1]%3==0) or (j == (result[-1] // 2) and result[-1]%2==0) or j == (result[-1] - 1):
            result.append(j)
            k -= 1
    
print(*result)