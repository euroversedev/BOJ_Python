import sys
N = int(input())
array = list(map(int, sys.stdin.readline().strip().split()))

dp = [1] * (N+1)

for i in range(1, N):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j]+1)
            
print(max(dp))


''' [review]
해당 문제는 N이 크지 않기 때문에
이중 반복을 통해 구현할 수 있었는데,
시간 초과가 걱정된다면

1. 탈출 조건을 걸어서 불필요한 연산줄이기
2. 다른 알고리즘으로 풀기

두 가지 해결책이 있다.
'''