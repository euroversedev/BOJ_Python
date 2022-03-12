import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

# visited에 [벽부수기전, 후] 상태의 거리를 따로 저장
visited = [[[-1, -1] for _ in range(M)] for _ in range(N)]

# bfs
def bfs():
    visited[0][0][0] = 1
    
    q = deque([(0, 0, 1, False)])    # (y, x, distance, 벽 부수기 여부)
    while q:
        y, x, dis, flag = q.popleft()

        # N, M에 도착
        if y == N-1 and x == M-1 and flag == False: return visited[-1][-1][0]
        if y == N-1 and x == M-1 and flag == True: return visited[-1][-1][1]
        
        for dy, dx in [(1,0), (-1,0), (0,1), (0, -1)]:
            if 0<=y+dy<N and 0<=x+dx<M:
                
                # 이동 가능한 칸 0을 만나면,
                if board[y+dy][x+dx] == 0:
                    if flag == False and visited[y+dy][x+dx][0] == -1:
                        visited[y+dy][x+dx][0] = dis+1
                        q.append((y+dy, x+dx, dis+1, flag))
                        
                    if flag == True and visited[y+dy][x+dx][1] == -1:
                        visited[y+dy][x+dx][1] = dis+1
                        q.append((y+dy, x+dx, dis+1, flag))
                
                # 벽 1을 만나면,
                if board[y+dy][x+dx] == 1 and flag == False:
                    visited[y+dy][x+dx][1] = dis+1
                    q.append((y+dy, x+dx, dis+1, True))
        
        
    return -1
                        

print(bfs())

'''
★ 아래 글 보길 바람..
진짜 핵심은 "벽을 만나면 Z축 한 칸 위로 올라간다는 발상"

이 문제의 핵심은
벽을 뚫었을 때와 뚫지 않았을 때 visited를 따로 처리해야한다는 것이다.
처음 만난 벽을 뚫기보다 두번째 벽을 뚫는 경로가 더 최적일 수 있기 때문.. 

https://www.acmicpc.net/board/view/85818

https://www.acmicpc.net/board/view/79649
★★3차원 배열을 사용하는 이유가 뭐죠..?
: 벽을 부쉈는데 또 부수면 안되기 때문에 그렇습니다.
3차원 배열에서 x축과 y축이 가로와 세로, z축이 벽을 부쉈는지 여부를 저장한다고 할 때,
아직 벽을 안 부순 경우는 벽을 만났을 때 벽을 부술 수 있고, 이 경우 3차원 배열 상에서 z축으로 이동합니다.
이미 벽을 부순 경우라면 벽을 만났을 때 벽을 부술 수 없습니다.
3차원 배열을 이용하면 이 과정을 현재 z축에서의 좌표를 통해 O(1)에 판단할 수 있습니다.
'''