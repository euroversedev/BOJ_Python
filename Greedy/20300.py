import sys

N = int(input())
array = list(map(int, sys.stdin.readline().strip().split()))
array.sort()

min_ = 0
# 홀수개인경우 => 제일 큰애만 분리시킴
if N % 2 == 1:
    min_ = array[-1]
    array.pop()
    
for i in range(len(array)//2):
    sum_ = array[i] + array[-1*i-1]
    if sum_ > min_ : min_ = sum_
        
print(min_)
