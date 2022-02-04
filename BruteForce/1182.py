import sys
from itertools import combinations

N, S = map(int, input().split())
array = list(map(int, sys.stdin.readline().split()))
cnt = 0
for i in range(1, N+1):
    combis = combinations(array, i)
    for combi in combis:
        if sum(combi) == S:
            cnt += 1
print(cnt)
