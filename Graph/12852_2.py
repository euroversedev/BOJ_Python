import sys

N = int(input())
dp = [10**6] * (N+1)
dp[N] = 0
for idx in range(N, 0, -1):
    
    if idx % 3 == 0:
        dp[idx//3] = min(dp[idx//3], dp[idx]+1)
    
    if idx % 2 == 0:
        dp[idx//2] = min(dp[idx//2], dp[idx]+1)
        
    if idx - 1 > 0:
        dp[idx-1] = min(dp[idx-1], dp[idx]+1)

print(dp[1])

sequence = [1]
while True:
    pre = sequence[-1]
    
    if pre == N:
        break
        
    if dp[pre] - 1 == dp[pre+1]:
        sequence.append(pre+1)
        continue
    
    if dp[pre] - 1 == dp[pre*2]:
        sequence.append(pre*2)
        continue
        
    if dp[pre] - 1 == dp[pre*3]:
        sequence.append(pre*3)
        continue
print(*sorted(sequence, reverse=True))
    

'''
DP를 이용해 푸는 방법
'''