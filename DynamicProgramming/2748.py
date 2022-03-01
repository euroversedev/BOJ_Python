dp = [0, 1] + [0] * 100
for i in range(2,100):
    dp[i] = dp[i-2] +dp[i-1]
print(dp[int(input())])