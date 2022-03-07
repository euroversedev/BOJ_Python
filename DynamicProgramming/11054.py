import  sys
N = int(input())
S = list(map(int, sys.stdin.readline().strip().split()))
len_ = len(S)

dp1 = [0] * len_
for i in range(len_):
    max_dp = 0
    for j in range(i):
        # 나보다 작은 애들중에 가장 큰 dp가져오기
        if S[i] > S[j] and max_dp < dp1[j]:
            max_dp = dp1[j]
        
    dp1[i] = max_dp+1

dp2 = [0] * len_
for i in range(len_-1, -1, -1):
    max_dp = 0
    for j in range(len_-1, i, -1):
        if S[i] > S[j] and max_dp < dp2[j]:
            max_dp = dp2[j]
    dp2[i] = max_dp+1
    

max_ = 0
for i in range(len_):
    if dp1[i]+dp2[i] > max_:
        max_ = dp1[i]+dp2[i]
print(max_-1)