import sys

N = int(input())
cost = [0] + list(map(int, sys.stdin.readline().strip().split()))
dp = [0] * (N+1)

for stride in range(1, N+1):
    for j in range(N+1-stride):
        if dp[j+stride] < dp[j] + cost[stride]:   
            dp[j+stride] = dp[j] + cost[stride]
        
print(max(dp))


''' [review]
dp[j+stride] = max(dp[j+stride] , dp[j] + cost[stride])에서
위 코드처럼 if문으로 조건 충족 시에만 대입하면 시간을 줄일 수 있음.
'''