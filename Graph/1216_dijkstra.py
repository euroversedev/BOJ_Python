import sys
import heapq

''' 다익스트라 최단 경로 알고리즘
양수 가중치가 있는 (= 간선의 w가 서로 다른) 그래프에서
시작 노드로부터 다른 모든 노드 까지의 최단 거리를 구하는 알고리즘
=> 한 번 반복할 때마다 노드 하나의 최단 경로가 확정되는 성질 (배낭)

1. 모든 노드까지의 거리는 무한대
2. 시작 노드 start까지의 거리는 0
=> 최솟값 선택을 반복 => 힙 자료형 사용
반 | 3. 힙에서 거리가 최소인 노드를 꺼냄 => 거리 확정
복 | 4. 그 노드로부터 인접한 노드들의 거리를 갱신
'''

M, N = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip()))
        for _ in range(N)]
dis = [[10**9] * M for _ in range(N)]

def dijkstra(start_y, start_x):
    dis[start_y][start_x] = 0
    h = [(start_y, start_x, dis[start_y][start_x])]
    
    while h:
        y, x, distance = heapq.heappop(h)
        
        if distance > dis[y][x]:
            continue
            
        for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
            if 0<=y+dy<N and 0<=x+dx<M:
                if dis[y+dy][x+dx] > distance+board[y+dy][x+dx]:
                    heapq.heappush(h, (y+dy, x+dx, distance+board[y+dy][x+dx]))
                    dis[y+dy][x+dx] = distance+board[y+dy][x+dx]
                    
dijkstra(0,0)
print(dis[N-1][M-1])