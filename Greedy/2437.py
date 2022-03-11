import sys

N = int(input())
array = list(map(int, sys.stdin.readline().strip().split()))

sum_ = 0
for num in sorted(array):

    if sum_+1 < num:
        break
        
    else:
        sum_ += num

print(sum_+1)
    
'''
https://www.acmicpc.net/board/view/45841
'''