import sys

dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + ([0] * 91)
for i in range(10, 101):
    dp[i] = dp[i-1] + dp[i-5]

T = int(input())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    print(dp[N-1])
    
''' [review]
모든 dp문제가
인덱스 초반부터 점화식이 적용되지는 않는다.
문제에서 앞에 케이스를 주는 경우에는 불규칙성 의심해보자
'''