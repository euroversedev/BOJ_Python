import sys
from bisect import bisect_left

N = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().strip().split()))

lis = [-10**10]
for num in array:
    if num > lis[-1]:
        lis.append(num)
        continue
    
    idx = bisect_left(lis, num)
    if idx >= len(lis):
        lis.append(num)

    else:
        lis[idx] = num

print(len(lis)-1)