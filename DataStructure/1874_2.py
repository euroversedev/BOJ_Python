import sys

N = int(input())
array = [int(sys.stdin.readline().strip()) for _ in range(N)]

i = 1
stack = []
result = []
for num in array:
    while i <= num:
        stack.append(i)
        result.append('+')
        i += 1
        
    if stack[-1] == num:
        stack.pop()
        result.append('-')

    
if stack:
    print("NO")
else:
    print(*result, sep='\n')
    