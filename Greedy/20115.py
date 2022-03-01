import sys

N = int(input())
array = list(map(int, sys.stdin.readline().strip().split()))
array.sort()

result = array[-1]
for quantity in array[:-1]:
    result += quantity / 2

print(result)