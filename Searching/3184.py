import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
board = [list(sys.stdin.readline().strip()) for _ in range(N)]
answer = {'v':0, 'o':0}

for i in range(N):
    for j in range(M):
        if board[i][j] in ['v', 'o']:
            
            # bfs
            cnt = {'v':0, 'o':0}
            cnt[board[i][j]] += 1
            board[i][j] = '#'
            
            q = deque([(i, j)])
            while q:
                y, x = q.popleft()
                for dy, dx in [(1,0),(0,1),(-1,0),(0,-1)]:
                    if 0<=y+dy<N and 0<=x+dx<M:
                        if board[y+dy][x+dx] != '#':
                            
                            if board[y+dy][x+dx] in ['v', 'o']:
                                cnt[board[y+dy][x+dx]] += 1
                                
                            board[y+dy][x+dx] = '#'
                            q.append((y+dy, x+dx))
                            
            
            if cnt['o'] > cnt['v']: answer['o'] += cnt['o']
            else: answer['v'] += cnt['v']
                
       
print(answer['o'], answer['v'])