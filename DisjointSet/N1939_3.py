import sys

N, M = map(int, input())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().strip().split()) 
    graph[a].append((b,c))
    graph[b].append((a,c))

def binary_search(start, end):
    mid = (start+end) // 2
    if start > end:
        return mid
    
    flag = bfs(x, y, mid)    # x에서 y로 mid무게로 갈 수 있는가
    if flag:
        a = binary_search(mid+1, end)
        
    else:
        binary_search(start, mid-1)

    
    


''' [review]
c의 범위에 대해 이진탐색으로 풀어보자
c가 최대 10억이므로 => 20, M이 최대 10만 => 20 * 10만 => 2천만번
연산으로 처리 가능할듯 약 1초 넘게?
'''