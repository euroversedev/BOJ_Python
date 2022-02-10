from itertools import permutations

N = int(input())
perms = permutations(range(1,N+1), N)
for perm in perms:
    print(*perm)