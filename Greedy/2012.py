import sys

N = int(input())
array = sorted([int(sys.stdin.readline().strip()) for _ in range(N)])

result = 0
for idx, expected in enumerate(array):
    result += abs(idx+1-expected)
print(result)
    