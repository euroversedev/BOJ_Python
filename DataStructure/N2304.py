import sys

N = int(input())
pipe = sorted([tuple(map(int, sys.stdin.readline().strip().split()))
               for _ in range(N)])

height = list(zip(*pipe))[1]
print(height)
print(pipe)

result = 0
def binary(start, end):
    max_idx = height.index(max(height[start:end+1]))
    print(max_idx)
    result +=
    
    left = binary(start, max_idx-1)
    right = binary(max_idx+1, end)
    
    
    
    
binary(0, N-1)


