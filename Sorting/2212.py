import sys

# 센서 N개
N = int(input())

# 집중국 K개
K = int(input())

# 센서의 좌표
array = sorted(list(map(int, sys.stdin.readline().strip().split())))


gap = []
for i in range(1, N):
    gap.append(array[i]-array[i-1])

print(sum(sorted(gap)[:N-K]))