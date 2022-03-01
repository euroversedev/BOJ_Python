import sys

N = int(input())
S = sys.stdin.readline().strip()
array = [int(sys.stdin.readline().strip()) for _ in range(N)]

stack = []
for ch in S:
    if ch.isalpha():
        stack.append(array[ord(ch)-ord('A')])
        continue
        
    b = stack.pop()
    a = stack.pop()
    
    if ch == '*': stack.append(a*b)
    if ch == '/': stack.append(a/b)
    if ch == '+': stack.append(a+b)
    if ch == '-': stack.append(a-b)
    
print(f"{stack[0]:.2f}")