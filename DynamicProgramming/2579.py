N = int(input())
array = [0] + [int(input()) for _ in range(N)]
dp = [0] * (N+1)

dp[N] = array[N]
dp[N-1] = array[N] + array[N-1]
dp[N-2] = max(array[N-2]+array[N], array[N-2]+array[N-1])

for i in range(N-3, 0, -1):
    dp[i] = array[i] + max(dp[i+2], array[i+1]+dp[i+3])

print(dp[1])



''' [review]
1. 마지막 도착 계단을 반드시 밟아야 한다는 조건
=> 앞전에 풀었던 문제들에는 없는 조건임. dp를 거꾸로 탐색해야한다는 힌트인듯
'''