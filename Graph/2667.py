import sys
from collections import deque

N = int(input())
array = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]
def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    
    cnt_home = 1
    while q:
        i, j = q.popleft()
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            if 0<=i+dx<N and 0<=j+dy<N:
                if visited[i+dx][j+dy] == False and array[i+dx][j+dy] ==1:
                    array[i+dx][j+dy] = 0
                    visited[i+dx][j+dy] = True
                    q.append((i+dx, j+dy))
                    cnt_home += 1
    
    return cnt_home

result = []
cnt = 0
for i in range(N):
    for j in range(N):
        if array[i][j] == 1:
            result.append(bfs(i, j))
            cnt += 1

result.sort()
print(cnt)
for i in range(len(result)):
    print(result[i])


''' [review]
단지에 속한 집의 수를 구하려면
DFS가 좋을까? BFS가 좋을까?
=> "재귀보단 반복문을 쓰는 BFS가 낫지 않을까?
반복마다 cnt증가하는 방식으로"라고 생각하고 풀이함
'''