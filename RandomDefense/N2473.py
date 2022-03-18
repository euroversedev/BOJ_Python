import sys
from bisect import bisect_left

N = int(input())
array = sorted(map(int, sys.stdin.readline().strip().split()))

min_abs = 10**9
min_set = set()
for i in range(N):
    a = array[i]
    for j in range(i+1, N):
        b = array[j]
        
        ''' a+b를 0으로 만들 가장 가까운 것을 찾으면 됨 '''
        idx = bisect_left(array[j+1:], -1*(a+b))
        
        if j<idx+j<N and min_abs > abs(a+b+array[idx+j]):
            min_abs = abs(a+b+array[idx+j])
            min_set = (a, b, array[idx+j])
            
        if j<idx-1+j<N and min_abs > abs(a+b+array[idx-1+j]):
            min_abs = abs(a+b+array[idx-1+j])
            min_set = (a, b, array[idx-1+j])
            
print(*sorted(min_set))