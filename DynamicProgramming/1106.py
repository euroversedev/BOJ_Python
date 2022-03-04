import sys

C, N = map(int, sys.stdin.readline().strip().split())
array = [tuple(map(int, sys.stdin.readline().strip().split()))
        for _ in range(N)]

# 사람 수를 나타내는 DP
dp = [0] * (C+1)
for i in range(1, C+1):
    min_ = 10**9
    for idx, (price, person) in enumerate(array):
        if 0 <= i-person and dp[i-person]+price < min_:
            min_ = dp[i-person]+price
    dp[i] = min_
print(dp)


''' review
위 코드는 정확히 C명일 때를 고려한 코드이다.

문제는 "적어도 C명" 이다.
'''