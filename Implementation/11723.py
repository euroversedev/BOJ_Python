import sys


S = set()
N = int(input())
for _ in range(N):
    cmd = sys.stdin.readline().strip()
    
    if 'add' in cmd:
        num = int(cmd[4:])
        if num not in S:
            S.add(num)
    
    if 'remove' in cmd:
        num = int(cmd[7:])
        if num in S:
            S.remove(num)
    
    if 'check' in cmd:
        num = int(cmd[6:])
        if num in S:
            print(1)
        else: print(0)
    
    if 'toggle' in cmd:
        num = int(cmd[7:])
        if num in S:
            S.remove(num)
        else: S.add(num)
            
    if 'all' in cmd:
        S.clear()
        S.update([i for i in range(1, 21)])
        
    if 'empty' in cmd:
        S.clear()
        
''' [review] 
remove는 없으면 Error,
discard는 없으면 pass => 이런 문제에서는 discard를 쓰자
'''