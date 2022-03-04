''' [ Dynamic Programming]

- DP에서 주로 쓰이는 전략
    1. 점화식 (ex. dp[i] = dp[i-1] + dp[i-2])
    2. 에라토스테네스의 체와 비슷한 유형
        => 매 반복마다 모든 dp[i]를 순회하면서 값을 업데이트함.

- 가장 좋은 예시
    2294번. 동전 2 (K원을 만들기 위한 최소 동전 수) 
    2293번. 동전 1 (K원을 만들는 경우의 수)
    => 동전 1 문제에서 i를 기준으로 했을 때와 코인을 기준으로 했을 때를 상기해보길 바람.
    => 코인을 기준으로 모든 i를 순회하면 중복을 제거할 수 있음.
'''



'''
다이나믹프로그래밍 빈출 유형 ex. 2294번 코인문제

대표적인 풀이 두가지
# 풀이 1: 코인의 가치를 내림차순 정렬 => 매 코인마다 dp를 순회하며 업데이트 (에라토스테네스의 체와 비슷)
# 풀이 2: 점화식으로 i번째 해당하는 dp를 구해나감 (걍 점화식)

'''

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

