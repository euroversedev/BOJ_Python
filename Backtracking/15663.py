from itertools import permutations

N, M = map(int, input().split())
array = map(int, input().split())

perms = set(permutations(sorted(array), M))
for perm in sorted(perms):
    print(*perm)