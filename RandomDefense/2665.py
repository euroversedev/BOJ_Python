import sys
from collections import deque

N = int(input())
board = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

# bfs
min_broken_black = [[10**9] * N for _ in range(N)] # `=. visited
q = deque([(0, 0, 0)])    # y, x, cnt_broken_black

while q:
    y, x, cnt_broken_black = q.popleft()
    
    for dy, dx in [(1,0),(0,1),(0,-1),(-1,0)]:
        if 0<=y+dy<N and 0<=x+dx<N:
            
            # 가려는 곳이 흰 방인 경우 => 그냥 가면 됨.
            if board[y+dy][x+dx] == 1:
                if cnt_broken_black < min_broken_black[y+dy][x+dx]:
                    min_broken_black[y+dy][x+dx] = cnt_broken_black
                    q.append((y+dy, x+dx, min_broken_black[y+dy][x+dx]))
            
            # 가려는 곳이 검은 방이면 => 부숴버리고, cnt ++
            if board[y+dy][x+dx] == 0:
                if cnt_broken_black + 1 < min_broken_black[y+dy][x+dx]:
                    min_broken_black[y+dy][x+dx] = cnt_broken_black + 1
                    q.append((y+dy, x+dx, min_broken_black[y+dy][x+dx]))
                    
print(min_broken_black[-1][-1])