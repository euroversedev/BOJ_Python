'''
DFS, BFS, Binary Search 관련 PS Skill입니다.
'''


해당 문제가 '깊이'와 '넓이' 중 어떠한 것을 구하는지 정확히 파악하고
알맞은 알고리즘을 적용해야 한다.
ex) BOJ_1325 효율적인 해킹문제는
얼마나 많은 컴퓨터로 뻗어나갈 수 있는지를 묻는 문제이므로
'깊이'가 아닌 '넓이'를 구하는 문제이다.


최대 깊이를 구하는 문제 :
    - DFS로 MAX(DFS(인접정점))+1로 구할 수 있다.
    - BFS에서 튜플을 이용해 깊이를 전달할 수 있다.
    - 시작점으로부터 모든 노드의 거리 => BFS를 이용해 배열에 저장
    
    
최대 넓이(면적)을 구하는 문제(BOJ_1325):
    - BFS로 큐의 popleft 횟수를 센다.
    - DFS로 SUM(DFS(인접정점))+1, 여기서 1은 자기 자신.
    
    넓이 구하기 가장 좋은 예시가 1926번인듯. DFS와 BFS 모두 가능


setrecursionlimit은 미리 메모리를 할당해놓는 느낌이어서
잘못 사용하면 메모리 초과를 유발할 수 있다.

''' [review]
500x500 인 경우, dfs(재귀)로 풀면
재귀가 쌓이면서 메모리 초과가 나온다. (재귀 스택오버플로우)
=> BFS로 풀자.
BFS 면적 구하기 == Popleft 몇번 하는지 세기

속도, 메모리 측면에서 dfs보다는 bfs가 우세하다. bfs 사용할 수 있으면 쓰자.
dfs는 백트래킹에나 잘 써먹자구.
'''


'''12852. 1로 만들기(2)에 관하여..
풀이법이 다양하다.
1. DP
2. dfs + dp
3. bfs 등

이 때, 문제 조건을 만족하는 수열을 만들기 위해 나는 역추적을 사용했다.
하지만, 아래와 같이 수열을 저장하면서 하는 코드가 있다.
=> 하나의 수열만 얻을 수 있는 역추적과 달리,
조건을 만족하는 "모든" 수열을 찾을 수 있다.

잊지말자, "최단경로"는 BFS.
'''
from collections import deque

n = int(input())
visited = [0] * (n+1)

q = deque([(n, [n])])
while q:
    num, answer_arr = q.popleft()
    if num == 1:
        print(len(answer_arr)-1)
        print(*answer_arr)
        break
    if not visited[num]:
        visited[num] = 1
        if num % 3 == 0:
            q.append((num//3, answer_arr+[num//3]))
        if num % 2 == 0:
            q.append((num//2, answer_arr+[num//2]))
        q.append((num-1, answer_arr+[num-1]))