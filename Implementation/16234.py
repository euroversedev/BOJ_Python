import sys
from collections import deque

# N by N matrix, L이상 R이하
N, L, R = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split()))
        for _ in range(N)]

answer = 0
while True:
    flag = True
    # print(graph)
    # 인구 이동
    visited = [[False] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if visited[y][x] == False:
                flag = False
                sum_ = board[y][x]
                tmp = []
                tmp.append((y, x))
                # bfs로 국경이 열린 도시들의 인구 총합을 구하고 다시 배분함.
                visited[y][x] = True
                q = deque([(y, x)])
                
                while q:
                    uy, ux = q.popleft()
                    # print(uy, ux)
                    for dy, dx in [(1, 0), (0, 1)]:
                        if uy+dy<N and ux+dx<N:
                            if L<=abs(board[uy][ux]-board[uy+dy][ux+dx])<=R:
                                vy, vx = uy+dy, ux+dx
                                if visited[vy][vx] == False:
                                    visited[vy][vx] = True
                                    q.append((vy, vx))
                                    sum_ += board[vy][vx]
                                    tmp.append((vy, vx))
                    
                # print(sum_)
                avg = sum_ // len(tmp)
                for i, j in tmp:
                    board[i][j] = avg
    
    if flag:
        print(answer)
        exit()
    # answer
    answer += 1

