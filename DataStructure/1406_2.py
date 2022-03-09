import sys
from collections import deque

S = list(sys.stdin.readline().strip())

# 커서 오른쪽을 저장할 서브 스택
stack = []

N = int(input())
for _ in range(N):
    cmd = list(sys.stdin.readline().strip())
    
    if cmd[0] == 'L':
        if S:
            stack.append(S.pop())
        continue
        
    if cmd[0] == 'D':
        if stack:
            S.append(stack.pop())
    
    if cmd[0] == 'B':
        if S:
            S.pop()
        
    if cmd[0] == 'P':
        S.append(cmd[2])

while stack:
    S.append(stack.pop())
    
print(''.join(S))





''' review
1406_1.py를 참고하길 바람.

"리스트의 맨 뒤에서만 삽입/삭제하는 알고리즘 구현 => 스택(or 큐) 두 개로 구현"
=> 덱 하나로 구현하려고 했더니, 커서가 맨 처음이랑 마지막에 있을 때를 구별을 못하네..
=> 걍 큐 두개 쓰자

프린트 or 에디터(1406)과 같이
커서를 이용하거나 인덱스를 따로 저장해야하는 경우는
단순 구현으로 풀기보다는 자료구조를 이용하면 쉽게 풀 수 있음. 매우 중요!
"커서, 대기열, 인덱스 문제 = 자료구조"
'''