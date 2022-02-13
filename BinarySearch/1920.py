import sys
from bisect import bisect_left

N = int(input())
array1 = list(map(int, sys.stdin.readline().strip().split()))
array1.sort()
M = int(input())
array2 = list(map(int, sys.stdin.readline().strip().split()))

for num in array2:
    idx = bisect_left(array1, num)
    if idx != N and num == array1[idx]:
        print(1)
    else:
        print(0)