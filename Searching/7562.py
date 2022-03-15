import sys
from collections import deque

T = int(input())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    visited = [[False] * N for _ in range(N)]
    
    y_start, x_start = map(int, sys.stdin.readline().strip().split())
    y_end, x_end = map(int, sys.stdin.readline().strip().split())
    
    answer = 0
    
    # bfs
    visited[y_start][x_start] = True
    q = deque([(y_start, x_start, 0)])
    while q:
        y_now, x_now, depth = q.popleft()
        
        if y_now == y_end and x_now == x_end:
            answer = depth
            break
        
        for dy, dx in [(-2,-1),(-1,-2),(1,2),(2,1),(1,-2),(2,-1),(-2,1),(-1,2)]:
            if 0<=y_now+dy<N and 0<=x_now+dx<N:
                if visited[y_now+dy][x_now+dx] == False:
                    visited[y_now+dy][x_now+dx] = True
                    q.append((y_now+dy, x_now+dx, depth+1))
        
    print(answer)
                    