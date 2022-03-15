import sys

N, L = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

road = []
board_t = list(map(list, zip(*board)))
for i in range(N):
    road.append(board[i])
    road.append(board_t[i])

answer = 0
tmp = 0

for array in road:
    visited = [False] * N
    flag = True # 통행 가능 여부
    pre = array[0]
    for i in range(1, N):
        now = array[i]
        
        # 차이가 1 초과이면 통행 불가
        if abs(now-pre) > 1:
            flag = False
            break
            
        if abs(now-pre) == 0:
            pre = now
            continue
        
        # 오르막길을 만나면 이전 L개가 now-1이 맞는지 확인
        if pre < now:
            for j in range(i-1, i-L-1, -1):
                if 0<=j<N and array[j] == now-1 and visited[j] == False:
                    visited[j] = True
                    continue
                else:
                    flag = False
                    break
            pre = now
        
        # 내리막길을 만나면 이후 L개가 pre-1이 맞는지 확인
        if pre > now:
            for j in range(i, i+L):
                if 0<=j<N and array[j] == pre-1 and visited[j] == False:
                    visited[j] = True
                    i += 1 
                    continue
                else:
                    flag = False
                    break
            pre = now
            
    if flag:
        print(array)
        answer += 1
        
print(answer)
    