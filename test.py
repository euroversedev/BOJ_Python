N = int(input())
dp = [1] * (N+1)
for i in range(2, N+1):
    dp[i] = (dp[i-1]*i)%15746

sum_ = 0
for i in range((N//2)+1):
    k = N-2*i
    sum_ += dp[i+k]//dp[i]//dp[k]
print(sum_%15746)