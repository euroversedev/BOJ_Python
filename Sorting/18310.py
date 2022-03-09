import sys

N = int(input())
array = sorted(list(map(int, sys.stdin.readline().strip().split())))        
print(array[(N-1)//2])