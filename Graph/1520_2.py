import sys
sys.setrecursionlimit(10**9)

N, M = map(int, input().split())
board = [list(map(int, sys.stdin.readline().strip().split()))
        for _ in range(N)]

# 2차원 리스트를 인덱스를 기억해서 정렬하려면 새롭게 만들어 줘야 할듯
# 정렬 한 후에는 선형 탐색이라서 괜찮으니, 정렬에서 시간을 줄여보자

board2 = [()] * N * M
k = 0
for i in range(N):
    for j in range(M):
        board2[k] = (board[i][j], i, j)
        k += 1
        
sorted_board = sorted(board2, key = lambda x:-x[0])
dp = [[0] * M for _ in range(N)]
dp[0][0] = 1
for i in range(1, len(sorted_board)):
    h, y, x = sorted_board[i]
    
    for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
        if 0<=y+dy<N and 0<=x+dx<M:
            if h < board[y+dy][x+dx]:
                dp[y][x] += dp[y+dy][x+dx]

#print(sorted_board)
#print(*dp, sep='\n')
print(dp[N-1][M-1])


''' [review]
500*500을 재귀로 완전 탐색하면 시간 초과
=> DP로 풀어보자.
DP로 풀려고 했더니 어떤 순서로 나열하지?
=> 정렬순으로 가자
'''