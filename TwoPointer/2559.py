import sys

N, K = map(int, input().split())
array = list(map(int, sys.stdin.readline().strip().split())) + [0]

start =0
end = K-1
sum_ = sum(array[:K])

max_ = - 10**6
for _ in range(N-K+1):
    if sum_ > max_: max_ = sum_
    
    sum_ -= array[start]
    start, end = start+1, end+1
    sum_ += array[end]
    
    if end == N: break
    
print(max_)