import sys
from collections import deque

N, M = map(int, input().split())
array = [i for i in range(1, N+1)]
a = deque(array)
b = deque()

i = 0
seq = []
while a or b:
    i += 1
    
    if not a:
        while b:
            a.append(b.popleft())

    
    if i == M:
        seq.append(a.popleft())
        i = 0
    
    else:
        b.append(a.popleft())

    
print("<", end="")
print(*seq, sep=', ', end="")
print(">")

''' [review]
리스트의 원소 삭제
인덱스로 삭제 : del array[idx] or del array[idx1:idx2]
값으로 삭제 : array.remove(value)
인덱스 삭제 후 값 반환하기 : array.pop(idx)

인덱스를 len(array)로 나눠주면 로테이션과 같은 결과이다
ex. idx = (idx+K) % len(array)

'''