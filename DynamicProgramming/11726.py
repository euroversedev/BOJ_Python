dp = [0, 1, 2] + [0] * 998
for i in range(3, 1001):
    dp[i] = dp[i-1] + dp[i-2]

N = int(input())
print(dp[N]%10007)


