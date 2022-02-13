import sys

''' [review]
이진 탐색의 목적은 탐색 속도를 빠르게 함에 있지만,
그것의 매력은 "탐색 범위를 좁혀나감"에 있다.
이 문제처럼 큰 범위가 주어졌을 때 이진 탐색을 떠올려보자.

=> N이 최대 100만개여서 for문을 돌리면 매반복마다 100만번 연산하는데,
반복문 돌리는 횟수를 획기적으로 줄이면 된다는 마인드
ln10억이 약 20정도임. 따라서, 2000만번 정도 연산함.
'''

N, M = map(int, input().split())
heights = list(map(int, sys.stdin.readline().split()))
heights.sort()

def binary_search(array, start, end, target):
    mid = (start + end) // 2
    
    if start > end:
        return mid
    
    sum_ = sum([num - mid for num in array if num > mid])
    
    if sum_ == target:
        return mid
        
    elif sum_ > target:
        return binary_search(array, mid+1, end, target)
    
    else:
        return binary_search(array, start, mid-1, target)
    
result = binary_search(heights, 0, max(heights), M)
print(result)