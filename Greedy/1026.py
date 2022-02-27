import sys

N = int(input())
A = sorted(list(map(int, sys.stdin.readline().strip().split())))
B = sorted(list(map(int, sys.stdin.readline().strip().split())), reverse = True)
print(sum(list(i * j for i, j in zip(A, B))))