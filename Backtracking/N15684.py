import sys
import copy
sys.setrecursionlimit(10**6)

# 세로선 N, 가로선 M, 점선 H
N, M, H = map(int, sys.stdin.readline().strip().split())

# 사다리 생성
board = [[None] * (N+1) for _ in range(H+1)]
for x in range(1, N+1):
    for y in range(1, H+1):
        board[y][x] = (y+1, x)
        
# 사다리를 놓을 수 있는 후보들 tmp
tmp = []
for y in range(1, H+1):
    for x in range(1, N+1):
        tmp.append((y, x))

# print(*board,sep='\n')

for _ in range(M):
    # b와 b+1을 잇는 a번째 점선을 실선으로 변경
    a, b = map(int, sys.stdin.readline().strip().split())
    board[a][b] = (a+1, b+1)
    board[a][b+1] = (a+1, b)
    tmp.remove((a, b))
    tmp.remove((a, b+1))
            
# print(*board,sep='\n')

def check(ladder):
    for i in range(1, N+1):
        y = 1
        x = i
        while y < N+1:
            y, x = ladder[y][x] 
        
        if x != i:
            return False
    return True
            
result = []
# 백트래킹으로 실선을 추가
def dfs(ladder, depth, tmp):
    print(*ladder, sep='\n')
    print(tmp)
    print()
    if depth > 3:
        return
    
    if check(ladder):
        result.append(depth)
    
    # tmp는 사다리를 놓을 수 있는 후보들이 저장됨.
    for y, x in tmp:
        print(y, x)
        if x + 1 >= N:
            continue
            
        if ladder[y][x] == (y+1, x) and ladder[y][x+1] == (y+1, x+1):
            ladder[y][x] = (y+1, x+1)
            ladder[y][x+1] = (y+1, x)
            tmp.remove((y, x))
            tmp.remove((y, x+1))
            dfs(ladder, depth+1, tmp)
            
            # 원상복구
            ladder[y][x] = (y+1, x)
            ladder[y][x+1] = (y+1, x+1)
            tmp.append((y, x))
            tmp.append((y, x+1))

dfs(board, 0, tmp)
print(result)
if result:
    print(min(result))
else:
    print(-1)
                