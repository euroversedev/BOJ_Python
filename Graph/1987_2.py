import sys
from collections import deque
import copy

N, M = map(int, sys.stdin.readline().strip().split())
board = [list(sys.stdin.readline().strip()) for _ in range(N)]

'''
bfs로 하면 메모리 초과 나려나 
=> 시간초과남 아래코드.. 알고리즘은 얼추 맞음
'''
max_len = 0

# bfs
visited = [False] * 26
visited[ord(board[0][0])-ord('A')] = True
q = deque([(0, 0, visited, 1)])
while q:
    y, x, array, len_array = q.popleft()
    
    if len_array > max_len:
        max_len = len_array
    
    for dy, dx in [(0,1),(0,-1),(1,0),(-1,0)]:
        if 0<=y+dy<N and 0<=x+dx<M:
            if array[ord(board[y+dy][x+dx])-ord('A')] == False:
                array2 = array[:]
                array2[ord(board[y+dy][x+dx])-ord('A')] = True
                q.append((y+dy, x+dx, array2, len_array+1))

print(max_len)
    