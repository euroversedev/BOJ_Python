import sys
from collections import deque

# N by N matrix, L이상 R이하
N, L, R = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split()))
        for _ in range(N)]

answer = 0
while True:
    # print(*board, sep='\n')
    # print()
    graph = dict()
    
    # 이동 가능한 국경선 구하기 => 간선으로 만듦
    cnt = 0
    for y in range(N):
        for x in range(N):
            # 아래 도시와의 간선 생성
            if y+1 < N and L<=abs(board[y][x]-board[y+1][x])<=R:
                if (y, x) not in graph: graph[(y, x)] = []
                graph[(y, x)].append((y+1, x))
                if (y+1, x) not in graph: graph[(y+1, x)] = []
                graph[(y+1, x)].append((y, x))
                cnt += 1
                
            # 오른쪽 도시와의 간선 생성
            if x+1 < N and L<=abs(board[y][x]-board[y][x+1])<=R:
                if (y, x) not in graph: graph[(y, x)] = []
                graph[(y, x)].append((y, x+1))
                if (y, x+1) not in graph: graph[(y, x+1)] = []
                graph[(y,x+1)].append((y, x))
                cnt += 1
    
    # 종료 조건 : 이동 가능한 국경선이 없는 경우
    if cnt == 0:
        break
    
    # print(graph)
    # 인구 이동
    visited = [[False] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            
            if visited[y][x] == False:
                sum_ = board[y][x]
                tmp = [(y, x)]
                # bfs로 국경이 열린 도시들의 인구 총합을 구하고 다시 배분함.
                visited[y][x] = True
                q = deque([(y, x)])
                
                while q:
                    uy, ux = q.popleft()
                    # print(uy, ux)
                    if (uy, ux) in graph:
                        for vy, vx in graph[(uy, ux)]:
                            # print(vy, vx)
                            if visited[vy][vx] == False:
                                visited[vy][vx] = True
                                q.append((vy, vx))
                                sum_ += board[vy][vx]
                                tmp.append((vy, vx))
                # print(sum_)
                avg = sum_ // len(tmp)
                for i, j in tmp:
                    board[i][j] = avg
    
    # answer
    answer += 1
    
print(answer)