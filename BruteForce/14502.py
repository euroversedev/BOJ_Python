from itertools import combinations
import copy
from collections import Counter, deque

N, M = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]

def bfs(array, i, j):    # array[i][j]는 바이러스 위치
    q = deque()
    q.append((i,j))
    
    while q:
        y, x= q.popleft()
        for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
            if 0<=y+dy<N and 0<=x+dx<M:
                if array[y+dy][x+dx] == 0:
                    array[y+dy][x+dx] = 2
                    q.append((y+dy, x+dx))

def solution(array2):    # 안전 영역의 크기 구하기
    for i in range(N):
        for j in range(M):
            if array2[i][j] == 2:
                bfs(array2, i, j)
                
    cnt = 0
    for i in range(N):
        for j in range(M):
            if array2[i][j] == 0:
                cnt += 1
    return cnt
    
# 0인 것 중에 벽을 세울 3개의 좌표 Combination
list_ = []
for i in range(N):
    for j in range(M):
        if array[i][j] == 0:
            list_.append((i, j))

MAX = 0
combis = combinations(list_,3)
for combi in combis:
    array2 = copy.deepcopy(array)
    for i, j in combi:
        array2[i][j] = 1
    tmp = solution(array2)
    if MAX < tmp: MAX = tmp

print(MAX)

''' [review]
solution 함수에서 매번 바이러스의 위치를 찾아서
bfs를 돌리는데, 바이러스 위치는 고정이니까 따로 변수에 저장해서 쓰자.

'''
    