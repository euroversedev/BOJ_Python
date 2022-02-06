import copy
N = int(input())

# 체스판에서 퀸의 위치와 퀸이 공격 가능한 위치는 True로 표시
board = [[False] * N for _ in range(N)]
cnt = 0

stack = []
def dfs(board,startY,startX):
    print(*board, sep='\n')
    print(stack)
    global cnt

    if len(stack) == N:
        cnt += 1
        return 
    
    for i in range(startY, N):
        for j in range(startX, N):
            if board[i][j] == False:
                # 퀸의 위치와 공격 가능한 위치를 모두 True로 표시
                flag = True
                board[i][j] = True
                for k in range(1, N):
                    for dy, dx in [(k,k),(k,-k),(-k,k),(-k,-k)
                                  ,(k,0),(-k,0),(0,k),(0,-k)]:
                        if 0<=i+dy<N and 0<=j+dx<N:
                            if board[i+dy][j+dx] == False:
                                board[i+dy][j+dx] = True
                            
                            if (i+dy, j+dx) in stack:
                                flag = False
                if flag:
                    stack.append((i, j))                
                    dfs(board, startY, startX)
                    stack.pop()
    return

for i in range(N):
    for j in range(N):
        dfs(copy.deepcopy(board), i, j)
print(cnt)
    

''' [review]
백트래킹의 대표격인 N-Queen 문제이다.
백트래킹은 보통 dfs(like 재귀)로 가지치기하며 푼다.
'''