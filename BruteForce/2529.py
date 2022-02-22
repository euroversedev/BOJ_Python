from itertools import permutations

K = int(input())
array = list(input().split())

min_, max_ = 10**10, -(10**10)
min_perm, max_perm = None, None
perms = permutations(range(10), K+1)
for perm in perms:
    flag = True
    for i in range(K):
        if array[i] == '<':
            if perm[i] > perm[i+1]:
                flag = False
                break
                
        elif array[i] == '>':
            if perm[i] < perm[i+1]:
                flag = False
                break
    
    if flag:
        n = int(''.join(list(map(str, perm))))
        if n > max_:
            max_ = n
            max_perm = perm
        if n < min_: 
            min_ = n
            min_perm = perm
            
print(''.join(list(map(str, max_perm))))
print(''.join(list(map(str, min_perm))))