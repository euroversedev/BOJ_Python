from itertools import product

N, M = map(int, input().split())
array = map(int, input().split())

perms = product(array, repeat=M)
for perm in sorted(perms):
    print(*perm)