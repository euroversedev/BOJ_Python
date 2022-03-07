import sys

N = int(input())

# (최대, 최소)
dp = [(0,0)] * 3

for _ in range(N):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    
    dp = [(a+max(dp[0][0], dp[1][0]), a+min(dp[0][1], dp[1][1])),
          (b+max(dp[0][0], dp[1][0], dp[2][0]), b+min(dp[0][1], dp[1][1], dp[2][1])),
          (c+max(dp[1][0], dp[2][0]), c+min(dp[1][1], dp[2][1]))]

result = list(zip(*dp))
print(max(result[0]), min(result[1]))
    
# board = [list(map(int, sys.stdin.readline().strip().split()))
#         for _ in range(N)]

# # 최대 점수 구하기
# dp = board[0]
# pre = [0] * 3
# for i in range(1, N):
#     pre[0] = board[i][0] + max(dp[0], dp[1])
#     pre[1] = board[i][1] + max(dp[0], dp[1], dp[2])
#     pre[2] = board[i][2] + max(dp[1], dp[2])
    
#     dp = pre[:]

# max_ = max(dp)

# # 최소 점수 구하기
# dp = board[0]
# for i in range(1, N):
#     pre[0] = board[i][0] + min(dp[0], dp[1])
#     pre[1] = board[i][1] + min(dp[0], dp[1], dp[2])
#     pre[2] = board[i][2] + min(dp[1], dp[2])
    
#     dp = pre[:]

# min_ = min(dp)

# print(max_, min_)
