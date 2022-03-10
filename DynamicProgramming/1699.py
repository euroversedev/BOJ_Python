N = int(input())

dp = [0, 1, 2, 3] + [0] * (N-3)

for i in range(4, N+1):
    
    min_dp = 10**9
    for j in range(1, int(i**0.5)+1):
        if min_dp > dp[i-j*j]:
            min_dp = dp[i-j*j]
    
    dp[i] = min_dp +1

print(dp[N])
