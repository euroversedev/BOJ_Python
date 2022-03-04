import sys

N, K = map(int, sys.stdin.readline().strip().split())
dp = [0] * (K+1)

coins = [int(sys.stdin.readline().strip()) for _ in range(N)]
dp[0] = 1
for coin in coins:
    for i in range(1, K+1):
        if 0 <= i - coin:
            dp[i] += dp[i-coin]


if dp[-1] != 10**9: print(dp[-1])
else: print(-1)


''' review

2294 동전 2번이랑 비슷한데

중요한 부분은 이중반복문에서 코인을 기준으로 모든 i를 순회할 것인지,
모든 i를 기준으로 코인을 순회할 것인지에 따라서 답이 매우 많이 달라진다는 것임.

아래는 내가 첫번째 풀었던 코드
for i in range(1, K+1):
    for coin in coins:
        if 0 <= i - coin:
            dp[i] = min(dp[i], dp[i-coin] +1 )
dp의 모든 i를 기준으로 매 반복마다 코인들을 순회하게 되면
=> 3원을 만들기위해 (1,1,1) (1,2) (2,1) 이렇게 세가지가 만들어짐.

그러나 문제 조건에 따라 (1,2)와 (2,1)은 중복이라 제거해야함.
이를 위해 => 코인을 기준으로 모든 i를 순회하는 전략을 쓸 수 있음
=> (1,1,1) (1,2)로 바뀌게 됨.

'''