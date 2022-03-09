import sys

S = list(sys.stdin.readline().strip())
cursor = len(S)

N = int(sys.stdin.readline().strip())
for _ in range(N):
    cmd = sys.stdin.readline().strip()
    
    if cmd[0] == 'L':
        if 0 <= cursor -1:
            cursor -= 1
        continue
    
    if cmd[0] == 'D':
        if cursor + 1 <= len(S):
            cursor += 1
        continue
    
    if cmd[0] == 'B':
        if 0 <= cursor-1:
            del S[cursor-1]
            cursor -= 1
        continue
    
    if cmd[0] == 'P':
        S = S[:cursor] + [cmd[2]] + S[cursor:]
        cursor += 1
        
print(''.join(S))

''' [review]
https://www.acmicpc.net/board/view/54572

del S[cursor-1] 과 S = S[:cursor] + [cm...의 시간 복잡도가 O(N)인 것에 주목하자.
파이썬 리스트는 연속된 메모리 공간을 할당해서 자료를 저장하므로,
리스트의 한가운데에 원소를 삽입/삭제하기 위해서는 그 자리 이후의 원소를 모두 밀거나 당겨야 한다.

이 문제를 해결하기 위해서는 다음 중 한가지를 선택해야 한다.
1. 리스트의 맨 뒤에서만 삽입/삭제하는 알고리즘 구현 => 스택(or 큐) 두 개로 구현
2. 한 가운데의 원소를 삽입/삭제했을 때 이외의 원소는 건드릴 필요가 없는 자료구조 사용 => Linked List



'''
    