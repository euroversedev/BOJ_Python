import sys
M, N, H = map(int, input().split())
array = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

print(array[0])
print(array[1])