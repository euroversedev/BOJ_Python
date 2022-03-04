from itertools import permutations

N, M = map(int, input().split())
array = map(int, input().split())

perms = permutations(array, M)
for perm in sorted(perms):
    print(*perm)