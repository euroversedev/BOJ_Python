import sys

N, M = map(int, sys.stdin.readline().strip().split())
array = [0] + list(map(int, sys.stdin.readline().strip().split()))
for i in range(1, N+1):
    array[i] += array[i-1]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    print(array[b] - array[a-1])