import sys
N = int(input())
array = sorted(list(tuple(map(int, sys.stdin.readline().strip().split()))
                   for _ in range(N)) , key = lambda x: (x[0], x[1]))
for i in range(N):
    print(*array[i], sep=' ')