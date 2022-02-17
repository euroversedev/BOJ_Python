import sys

dp = [1] * 30
for i in range(2,30):
    dp[i] = dp[i-1] * i


T = int(input())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().strip().split())
    print(dp[b]//dp[b-a]//dp[a])


''' [review]
조합 사용하면 시간초과

import sys
from itertools import combinations

T = int(input())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().strip().split())
    arr1 = list(range(b))
    print(len(list(combinations(arr1, b-a))))

'''