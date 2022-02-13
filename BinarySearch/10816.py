import sys
from bisect import bisect_left, bisect_right

N = int(input())
array1 = sorted(list(map(int, sys.stdin.readline().strip().split())))
M = int(input())
array2 = list(map(int, sys.stdin.readline().strip().split()))

for num in array2:
    left_ = bisect_left(array1, num)
    right_ = bisect_right(array1, num)
    
    if left_ != N and array1[left_] == num:
        print(right_-left_, end=' ')
    else:
        print(0, end=' ')

''' [review]
계수 정렬에서 처럼 한번의 for문으로 갯수 세서 할 수도 있음
=> 메모리가 걱정된다면 리스트가 아닌 dict()로 선언하면 됨.
'''