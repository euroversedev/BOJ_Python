import sys
from bisect import bisect_left

N = int(input())
array = list(map(int, sys.stdin.readline().split()))

set_ = set()
for n in array:
    set_.add(n)

set_ = sorted(list(set_))
    
for n in array:
    idx = bisect_left(set_, n)
    print(idx, end=' ')