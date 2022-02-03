import sys

stack = []

N = int(input())
for _ in range(N):
    s = sys.stdin.readline().strip().split()

    if 'push' in s:
        stack.append(int(s[1]))
    
    if 'top' in s:
        if len(stack) == 0:
            print("-1")
        else: print(stack[-1])
    
    if 'pop' in s:
        if len(stack) == 0:
            print("-1")
        else: print(stack.pop())
    
    if 'size' in s:
        print(len(stack))
    
    if 'empty' in s:
        if len(stack) == 0: print("1")
        else: print("0")