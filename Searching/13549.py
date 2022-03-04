from collections import deque

N, K = map(int, input().split())

visited = set()

def bfs(N, K):
    visited.add(N)
    q = deque([(N, 0)])    
    
    while q:
        x, depth = q.popleft()
        print(x, depth)
        if x == K:
            return depth
        
        for k in [2*x, x-1, x+1]:
            if 0<=k<=200000 and k not in visited:
                visited.add(k)
                
                if k != 2*x:
                    q.append((k, depth+1))
                if k == 2*x:
                    q.append((k, depth))
                
    return -1
        
print(bfs(N, K))


''' review
이 문제의 핵심은 큐에서 가져올 떄 depth가 작은 것부터 가져오기 위해
for문에서 반복 순서를 적절히 정하는 것이다.

4->6인 경우에 (4,3,6)이 (4,5,6)보다 빠르다는 것을 인지하자.

for문 돌 때, [2*x, x-1, x+1]와 [x-1, x+1, 2*x]의 차이를 생각해보길 바람.
2*x의 경우 depth를 추가하지 않기 때문에 x-1, x+1보다 우선 탐색되어야 함.
=> 2->27의 경우에
[2*x, x-1, x+1]: 2 4 8 7 14 28 27 => 3
[x-1, x+1, 2*x]: 2 3 6 12 13 26 27 => 4

'''