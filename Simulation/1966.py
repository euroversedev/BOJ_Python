import sys
from collections import deque

T = int(input())
for i in range(T):
    N, idx = map(int, input().split())
    array = list(map(int, sys.stdin.readline().strip().split()))
    q = deque(array)
    
    cnt = 0
    while q:
        now = q.popleft()
        
        
        flag = True
        for i in range(len(q)):
            if now < q[i]:
                q.append(now)
                flag = False
                break
        
        if flag:
            cnt += 1
            if idx == 0:
                print(cnt)
                break
        
        idx = (idx-1)%len(q)
                
    
''' [review]
파이썬에는 포인터가 없다는 것을 명심하자.
일부 상황에서 변수 할당을 "포인터처럼" 사용할 수 있는데, 어디까지나 일부 상황이다.
id 값은 시스템 내부에 할당된 숫자에 불과하다. 포인터와는 다르다.
따라서, 이 문제는 M번째 문서를 포인터로 가리켜서 해결할 수는 없다.
ex. array[1,2,3,1]에서 0번 3번의 1은 id가 같다.
'''