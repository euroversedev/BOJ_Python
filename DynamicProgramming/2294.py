import sys

N, K = map(int, sys.stdin.readline().strip().split())
dp = [10**9] * (K+1)

# 풀이 1: 코인의 가치를 내림차순 정렬 => 매 코인마다 dp를 순회하며 업데이트
# 풀이 2: 점화식으로 i번째 해당하는 dp를 구해나감

# 아래는 풀이 2번
coins = [int(sys.stdin.readline().strip()) for _ in range(N)]
dp[0] = 0

for i in range(1, K+1):
    for coin in coins:
        if 0 <= i - coin:
            dp[i] = min(dp[i], dp[i-coin] +1 )

if dp[-1] != 10**9: print(dp[-1])
else: print(-1)


    