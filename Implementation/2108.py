import sys
from collections import Counter

N = int(input())
array = [int(sys.stdin.readline().strip()) for _ in range(N)]

len_array = len(array)
sum_array = sum(array)
array.sort()
a= int(round(sum_array/len_array, 0))
b = array[N//2]
count = Counter(array)
c = sorted(count.most_common(), key = lambda x: (-x[1], x[0]))
d = max(array) - min(array)


if len(c) > 1 and c[0][1] == c[1][1]:
    c = c[1][0]
else:
    c = c[0][0]

print(a, b, c,  d, end='\n')