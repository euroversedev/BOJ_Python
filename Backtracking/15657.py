from itertools import combinations_with_replacement

N, M = map(int, input().split())
array = map(int, input().split())

perms = combinations_with_replacement(sorted(array), M)
for perm in sorted(perms):
    print(*perm)