N = int(input())
dp = list(map(int, input().split()))

for i in range(1, N):
    a, b, c = map(int, input().split())
    x = min(a+dp[1], a+dp[2])
    y = min(b+dp[0], b+dp[2])
    z = min(c+dp[0], c+dp[1])
    dp = [x, y, z]

print(min(dp))