N = int(input())
dp = [1]*10
for k in range(N-1):
    for i in range(9,-1,-1):
        for j in range(i-1, -1, -1):
            dp[i] += dp[j]

print(sum(dp)%10007)
