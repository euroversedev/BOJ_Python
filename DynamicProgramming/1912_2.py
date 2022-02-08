import sys

N = int(input())
array = list(map(int, sys.stdin.readline().strip().split()))

sum_ = 0
max_sum = -10**9
for num in array:
    sum_ += num
    
    if max_sum < sum_: max_sum = sum_
    
    if sum_ < 0:
        sum_ = 0

print(max_sum)
