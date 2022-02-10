import sys
from itertools import permutations

N = int(input())
value = [list(map(int, sys.stdin.readline().strip().split()))
        for _ in range(N)]

min_ = 10**9
perms = permutations(range(N), N)
for perm in perms:
    sum_ = 0
    breaker = False
    for i in range(N):
        tmp = value[perm[i-1]][perm[i]]
        if tmp == 0:
            breaker = True
            break
            
        sum_ += value[perm[i-1]][perm[i]]
    if breaker:
        continue
    min_ = min(min_, sum_)
print(min_)

''' [review]
외판원 순회 문제는 영어로 Traveling Salesman problem (TSP) 라고 불리는 
문제로 computer science 분야에서 가장 중요하게 취급되는 문제 중 하나이다.
여러 가지 변종 문제가 있으나, 여기서는 가장 일반적인 형태의 문제를 살펴보자.

브루트 포스문제를 단순히 중첩 반복문으로 전수조사한다고 생각하지말자.
dfs를 이용한 백트래킹에서도 모든 조건을 훑기만 한다면 브루트포스의 일종이다.
'''