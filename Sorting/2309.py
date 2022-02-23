import sys
from itertools import combinations

array = [int(sys.stdin.readline().strip()) for _ in range(9)]
array.sort()

combis = combinations(array, 7)

for combi in combis:
    if sum(combi) == 100:
        print(*combi, sep='\n')
        break
    