import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(num):
    dis = [10**9] * (N+1)
    q = deque([(num, 0)])
    
    while q:
        num, distance = q.popleft()

        # 친구들 중에서
        for friend in graph[num]:
            # 방문한적 없으면 q에 넣기
            if dis[friend] == 10**9:
                q.append((friend, distance+1))
                dis[friend] = distance+1

    return sum(dis[1:])

list_ = []
for i in range(1, N+1):
    list_.append((i, bfs(i)))
    
sorted_list = sorted(list_, key=lambda x : (x[1], x[0]))
print(sorted_list[0][0])

''' [review]
distance가 결정되는 시점에 주목하자.
한 정점이 q에 여러번 들어가는 경우가 있을 수 있다. (=여러 정점의 인접 정점인 경우)

큐에 넣어줄 때 방문여부를 확정한다(=최단거리를 확정한다)
=> BFS라서 처음 넣어줄 때 확정지어도 상관 없음.
=> 무엇보다, 한 번 넣었던게 다시 큐에 들어가는 일을 방지해줌.

'''