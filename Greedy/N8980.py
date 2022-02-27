import sys
from collections import deque
import heapq

N, C = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(N+1)]


M = int(sys.stdin.readline().strip())

for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().strip().split())
    graph[u].append((v, w))

result = 0
truck = deque()
sum_ = 0
for i in range(1, N+1):

    # 박스 내려주기
    while truck and truck[0][0] == i:
        result += truck[0][1]
        sum_ -= truck[0][1]
        truck.popleft()
        
    # 박스 풀어헤치기
    tmp = []
    while truck:
        heapq.heappush(tmp, truck.popleft())
        
    
    for j in range(len(graph[i])):
        heapq.heappush(tmp, graph[i][j])
    

    sum_ = 0
    while sum_ < C and tmp:
        v, w = heapq.heappop(tmp)
        truck.append((v, w))
        sum_ += w
    
    if sum_ > C:
        v, w = truck.pop()
        truck.append((v, w-sum_+C))
        sum_ = C

print(result)

''' review
더 가까운 짐으로 대체해서 싣고가는 알고리즘인데
구현이 어려운데..? 알고리즘 자체는 머리로 생각하기 쉬운데..


=> 박스를 대체해서 싣지말고 (= 계산이 너무 복잡한)
내가 들고 있던 박스들을 모두 풀어 놓고
정렬한 뒤에 가장 작은 번호의 박스로 채워 넣자. => 계산 쉬워짐.

결국 75점 부분점수 받음.. 시간 공간 복잡도 고려해서 100점 맞아보자..
=> https://jjangsungwon.tistory.com/114 이런 식으로 푸는 방법도 있네..

'''
        