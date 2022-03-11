import sys
import copy

N = int(input())
school = [list(sys.stdin.readline().strip().split()) for _ in range(N)]

teachers = []
for i in range(N):
    for j in range(N):
        if school[i][j] == 'T':
            teachers.append((i, j))

def dfs(board, cnt_O):
    if cnt_O == 3:
        # 선생의 눈을 피할 수 있으면 True를 return
        
        for y, x in teachers:
            for dy, dx in [(1,0),(0,1),(-1,0),(0,-1)]:
                k = 1
                while 0<=y+dy*k<N and 0<=x+dx*k<N:
                    if board[y+dy*k][x+dx*k] == 'O':
                        break

                    if board[y+dy*k][x+dx*k] == 'S':
                        return

                    k += 1
        
        print("YES")
        exit()
        
    for y in range(N):
        for x in range(N):
            if board[y][x] == 'X':
                board_forked = copy.deepcopy(board)
                board_forked[y][x] = 'O'
                dfs(board_forked, cnt_O+1)
                
dfs(school, 0)    
print("NO")