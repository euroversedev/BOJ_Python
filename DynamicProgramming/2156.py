N = int(input())
array = [int(input()) for _ in range(N)]

dp = array.copy()
if N >=2:
    dp[1] = dp[1]+dp[0]
if N>=3:
    dp[2] = max(dp[1], dp[2]+dp[0], dp[2]+array[1])

if N>=4:
    for i in range(3, N):
        dp[i] = max(array[i]+array[i-1]+dp[i-3], array[i]+dp[i-2], dp[i-1])
print(dp[N-1])


''' [review]
dp[i] = max(i번째 잔을 먹는 경우 2가지, 먹지 않는 경우 1가지)

이런 경우에는 항상 N이 굉장히 작은경우
1 or 2.. 까지 고려하자. 특히나 코테에서!

++ input()을 반복하는 경우는
sys.stdin.readline()으로 처리하자.
'''