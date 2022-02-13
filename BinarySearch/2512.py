import sys

N = int(input())
array = sorted(list(map(int, sys.stdin.readline().split())))
M = int(input())

sum_ = sum(array)
def binary_search(start, end):
    mid = (start+end) // 2
    
    if start > end:
        return mid
    
    over = sum([num - mid for num in array if num > mid])
    
    if sum_ - over == M:
        return mid
    elif sum_ - over < M:    # 예산을 만족하는 경우
        return binary_search(mid+1, end)
    else:
        return binary_search(start,mid-1)
    
print(binary_search(1, max(array)))