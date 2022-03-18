import sys
from collections import deque

T = int(input())
for _ in range(T):
    A, B = sys.stdin.readline().strip().split()
    A = ['0'] *(4-len(A)) + [A]
    B = int(''.join(B))
    
    visited = [False] * (20000)
    # bfs
    q = deque([(A, [])])
    while q:
        num, pre = q.popleft()

        if int(''.join(num)) == B:
            print(*pre, sep='')
            break
            
        tmp = list(str(int(''.join(num))*2%10000))
        D = ['0'] * (4-len(tmp)) + tmp
        
        tmp = list(str((int(''.join(num))-1)%10000))
        S = ['0'] * (4-len(tmp)) + tmp
        
        L = num[1:] + [num[0]]
        R = [num[3]] + num[:3]
        
        
        for K, ch in [(D, 'D'),(S, 'S'),(L, 'L'),(R, 'R')]:
            idx = int(''.join(K))
            if visited[idx] == False:
                visited[idx] = True
                q.append((K, pre+[ch]))
        
    