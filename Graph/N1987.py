import sys
sys.setrecursionlimit(10**9)
''' 1987번- DFS를 이용한 풀이 '''

'''
DFS 스택(재귀)를 이용한다.
자기 자신을 방문처리
자기 자신의 인접 노드를 하나씩 dfs

이 문제 질문을 보면 
공통적으로 시간초과 때문에 안풀리는듯
파이썬 언어으 한계인거같기도 풀이는 얼추 맞음

=> 1520번과 비슷하네
'''

N, M = map(int, input().split())
board = [list(sys.stdin.readline().strip()) for _ in range(N)]

visited = [False] * 26
max_ = 0
def dfs(i, j):
    global max_
    
    ch = board[i][j]
    visited[ord(ch)-ord('A')] = True
    
    # 최대값 갱신
    if max_ < sum(visited):
        max_ = sum(visited)
    
    for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
        if 0<=i+dy<N and 0<=j+dx<M:
            ch2 = board[i+dy][j+dx]
            if visited[ord(ch2)-ord('A')] == False:
                dfs(i+dy, j+dx)

dfs(0, 0)
print(max_)
    
