dp = [0, 1] + [0] * 19
for i in range(2,21):
    dp[i] = dp[i-2] +dp[i-1]
print(dp[int(input())])