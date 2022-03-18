import sys
from itertools import combinations, permutations

L, C = map(int, sys.stdin.readline().strip().split())
array = sorted(sys.stdin.readline().strip().split())

result = []
combis = combinations(array, L)
for combi in combis:
    cnt_a = 0
    cnt_b = 0
    flag = False
    for ch in combi:
        if ch in ['a', 'e', 'i', 'o', 'u']: cnt_a += 1
        else: cnt_b += 1
            
        if cnt_a > 0 and cnt_b > 1:
            flag = True
            break
    
    if flag:
        result.append(''.join(combi))

print(*result, sep='\n')

# aeiou = []
# bcdfg = []
# for ch in array:
#     if ch in ['a', 'e', 'i', 'o', 'u']:
#         aeiou.append(ch)
#     else: bcdfg.append(ch)
        
# result = []
# for k in range(1, L-1):
#     combis_aeiou = combinations(aeiou, k)
#     combis_bcdfg = combinations(bcdfg, L-k)
    
#     for combi_aeiou in combis_aeiou:
#         for combi_bcdfg in combis_bcdfg:
#             perms = combinations(combi_aeiou+combi_bcdfg, L)
#             for perm in perms:
#                 result.append(''.join(perm))
            
# print(*sorted(result))