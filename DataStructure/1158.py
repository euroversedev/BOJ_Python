from collections import deque

N, K = map(int, input().split())
q = deque([i for i in range(1, N+1)])
result = []

while q:

    for i in range(K-1):
        x = q.popleft()
        q.append(x)
    
    x = q.popleft()
    result.append(x)

    
print('<'+', '.join(map(str,result))+'>')
    
    
''' review
array.pop(idx)는 array[idx]에 해당하는 원소를 반환하고 삭제한다.
'''