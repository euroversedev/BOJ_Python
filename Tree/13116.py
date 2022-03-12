import sys

T = int(input())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().strip().split())
    
    set_A = set()
    while A > 0:
        set_A.add(A)
        A //= 2
    
    set_B = set()
    while B > 0:
        set_B.add(B)
        B //= 2
    
    print(max(set_A&set_B)*10)