import sys
from bisect import bisect_left

'''
bisect를 이용한 방법
'''

N, M = map(int, sys.stdin.readline().strip().split())

dict_ = dict()
values = []
for _ in range(N):
    title, upper_value = sys.stdin.readline().strip().split()
    if int(upper_value) not in dict_:
        dict_[int(upper_value)] = title
        values.append(int(upper_value))

for _ in range(M):
    power = int(sys.stdin.readline().strip())
    idx = bisect_left(values, power)
    print(dict_[values[idx]])