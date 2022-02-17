N = int(input())
dp = [0,0,1] + [0] * (N-2)

for i in range(3, N+1):
    tmp = [dp[i-1]+1]
    if i % 3 == 0: tmp.append(dp[i//3]+1)
    if i % 2 == 0: tmp.append(dp[i//2]+1)
    dp[i] = min(tmp)

print(dp[N])
        