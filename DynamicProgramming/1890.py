import sys
from collections import deque
sys.setrecursionlimit(10**6)

N = int(input())
board = [list(map(int, sys.stdin.readline().strip().split()))
        for _ in range(N)]

def bfs():
    q = deque([(0, 0)])
    
    cnt = 0
    while q:
        y, x = q.popleft()
        
        k = board[y][x]
        
        if k == 0:
            cnt += 1
            continue
        
        for dy, dx in [(k, 0), (0, k)]:
            if 0<=y+dy<N and x<=x+dx<N:
                q.append((y+dy, x+dx))
    return cnt

dp = [[0] * N for _ in range(N)]
def dfs(y, x):
    if dp[y][x] > 0:
        return dp[y][x]
    
    if y == N-1 and x == N-1:
        return 1
    
    k = board[y][x]
    if k == 0:
        return 0
    
    sum_ = 0
    for dy, dx in [(k, 0), (0, k)]:
        if 0<=y+dy<N and x<=x+dx<N:
            sum_ += dfs(y+dy, x+dx)
            
    if sum_ > 0:
        dp[y][x] = sum_
        
    return sum_


print(dfs(0, 0))


''' review
bfs로 풀면 11111이 반복되는 경우 오버플로우 => 메모리 초과
dfs + dp로 풀면 알고리즘 복잡해짐
그냥 dfs, bfs안쓰고 dp로 푸는게 제일 나을듯

'''