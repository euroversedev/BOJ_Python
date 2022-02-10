from itertools import permutations

N = int(input())
array = list(map(int, input().split()))

MAX = -10**9
perms = permutations(array, N)
for perm in perms:
    sum_ = 0
    for i in range(1, N):
        sum_ += abs(perm[i-1] - perm[i])
    
    if sum_ > MAX:
        MAX = sum_
print(MAX)