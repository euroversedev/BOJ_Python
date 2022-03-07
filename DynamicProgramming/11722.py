import  sys
N = int(input())
S = list(map(int, sys.stdin.readline().strip().split()))
len_ = len(S)


dp2 = [0] * len_
for i in range(len_-1, -1, -1):
    max_dp = 0
    for j in range(len_-1, i, -1):
        if S[i] > S[j] and max_dp < dp2[j]:
            max_dp = dp2[j]
    dp2[i] = max_dp+1
    
print(max(dp2))