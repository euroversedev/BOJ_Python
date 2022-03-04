from itertools import combinations

N, M = map(int, input().split())
array = map(int, input().split())

perms = combinations(sorted(array), M)
for perm in sorted(perms):
    print(*perm)