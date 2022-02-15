import sys

N = int(input())
stairs = [0] + [int(sys.stdin.readline().strip())
                for _ in range(N)]    # idx 0~N

if N > 2:
    dp = [0, stairs[1], stairs[1]+stairs[2]] + [0] * (N-2)

    for i in range(3, N+1):
        dp[i] = max(stairs[i]+stairs[i-1]+dp[i-3],
                   stairs[i]+dp[i-2])

else:
    dp = [0]
    for i in range(N):
        dp.append(sum(stairs[:i+2]))

print(dp[-1])


''' [review]
작은 인덱스에 대해 DP가 적용되지 않는 경우
직접 변수에 넣어주면 되고, 특히! N이 작은 테케에 주의하자.
위에서 처럼 else로 어렵게 굴지말고 아래처럼 간단하게 표현하자.
dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(s[1] + s[2], s[0] + s[2])
'''