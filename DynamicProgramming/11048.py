import sys

N, M = map(int, input().split())
array = [[0]*(M+1)] + [[0] + list(map(int, sys.stdin.readline().strip().split()))
                    for _ in range(N)]

for y in range(1, N+1):
    for x in range(1, M+1):
        array[y][x] += max(array[y-1][x], array[y][x-1], array[y-1][x-1])

print(array[-1][-1])