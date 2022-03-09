import sys
from bisect import bisect_left

N = int(input())
array = [(i, j) for j, i in sorted(enumerate(list(map(int, sys.stdin.readline().strip().split()))), key = lambda x: x[1])]

X = int(input())
cnt = 0
for i in array:
    left = bisect_left(array, (X-i[0], i[1]))

    while left < N and array[left][0] == X-i[0] and array[left][1] > i[1]:
        cnt += 1
        left += 1
        
print(cnt)
    