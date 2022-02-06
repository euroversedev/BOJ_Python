import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
city = [list(map(int, sys.stdin.readline().strip().split()))
       for _ in range(N)]

def distance(y1, x1, y2, x2):
    return abs(y1-y2)+abs(x1-x2)

# 집과 치킨집의 좌표를 저장
homes = []
chickens = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            homes.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

# 모든 집과 모든 치킨집 사이의 거리 구하기
d = [[] for _ in range(len(homes))]
for idx, home in enumerate(homes):
    for chicken in chickens:
        d[idx].append(distance(*home, *chicken))


# 치킨집 M개를 골랐을 때 각각의 거리의 합을 구하고 최소값을 저장
MIN = 10**9
combis = combinations(range(len(chickens)), M)
for combi in combis:
    sum_ = 0
    tmp = [[] for _ in range(len(homes))]
    for i in range(len(homes)):    # 모든 집에 대해 갱신
        tmp[i] = [d[i][j] for j in combi]
    min_ = [0] * len(homes)
    for i in range(len(homes)):
        min_[i] = min(tmp[i])
    
    sum_ = sum(min_)
    if sum_ < MIN:
        MIN = sum_

print(MIN)
''' [review]
설계:
N, M이 그리 크지 않아서 브루트 포스로 풀릴듯?
모든 집에 대해 각각의 치킨집 까지의 거리를 구하고
치킨집 M개를 골랐을 때 거리의 합을 구하자.

방법 1. 거리를 모두 구하고 치킨집을 선택해서 합 구하기
방법 2. 치킨집 선택해서 거리를 구하고 합 구하기

나는 방법 1로 했음.
방법 2로 하는 경우 치킨집을 선택할 때마다 거리를 다시 구해야해서
시간 복잡도가 커짐.
'''