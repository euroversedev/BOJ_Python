import sys

T = int(input())
for _ in range(T):
    s = sys.stdin.readline().strip()
    
    right = []
    left = []
    for ch in s:
        if ch.isalpha() or ch.isdigit():
            right.append(ch)
            continue
        
        if ch =='<' and right:
            left.append(right.pop())
            continue
            
        if ch =='>' and left:
            right.append(left.pop())
            continue
            
        if ch =='-' and right:
            right.pop()
            continue
    
    while left:
        right.append(left.pop())
    print(''.join(right))