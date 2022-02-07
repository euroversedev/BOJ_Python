import sys
from collections import Counter

N = int(input())
array = [int(sys.stdin.readline().strip()) for _ in range(N)]
count = Counter(array)
sorted_count = sorted(list(count.most_common()), key = lambda x: (-x[1], x[0]))
print(sorted_count[0][0])