import sys
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

dis = [[0] * M for _ in range(M)]
visit = [False] * 26
def  dfs(i, j, k):
    ch = board[i][j]
    visit[ord(ch)-ord('A')] = True
    dis[i][j] = max(dis[i][j], k)
    
    for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
        if 0<=i+dy<N and 0<=j+dx<M:
            ch = board[i+dy][j+dx]
            if visit[ord(ch)-ord('A')] == False:
                dfs(i+dy, j+dx, k+1)
                visit[ord(ch)-ord('A')] = False
    
dfs(0, 0, 1)
print(max(map(max, dis)))
    
