N = int(input())
dp = [10**9] * (N+1)

for i in range(int(N**0.5), 0, -1):
    x = 0
    
    for j in range(i*i, N+1, i*i):
        x += 1
        if dp[j] != 10**9:
            x = dp[j]
            continue
    
        dp[j] = x
print(dp)
print(dp[N])

        

    