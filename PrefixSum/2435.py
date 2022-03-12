import sys

N, K = map(int, sys.stdin.readline().strip().split())
array = list(map(int, sys.stdin.readline().strip().split()))

max_ = -1*10**4
for i in range(N-K+1):
    interval_sum = sum(array[i:i+K])
    if max_ < interval_sum: max_ = interval_sum

print(max_)