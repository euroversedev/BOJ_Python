N = int(input())
dp = [[0] * 10 for _ in range(N+1)]

dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(2, N+1):
    dp[i][0] = dp[i-1][1]
    for j in range(1, 9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    dp[i][9] = dp[i-1][8]


print(sum(dp[N])%(10**9))

''' [review]
dp[i][j]는 i자리 숫자에서 j로 시작하는 계단수 이다.
ex. dp[2][1] = 두자리 숫자 중 1로 시작하는 계단수, 10과 12
'''