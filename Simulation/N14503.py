import sys

N, M = map(int, input().split())
r, c, d = map(int, input().split())

# 0북, 1동, 2남, 3서
move = [[(0,-1),(1,0),(0,1),(-1,0)],    
       [(-1,0),(0,-1),(1,0),(0,1)],    
       [(0,1),(-1,0),(0,-1),(1,0)],   
       [(1,0),(0,1),(-1,0),(0,-1)]]    

array = [list(map(int, sys.stdin.readline().strip().split()))\
        for _ in range(N)]

cnt =0
def clean_up(y, x, d):
    global cnt
    global array
    
    if array[y][x] == 0:
        cnt += 1
        array[y][x] = 2    # 청소 완료 영역 == 2
    
    dd = d
    for dy, dx in move[d]:
        dd = (dd-1) % 4 
        if 0<=y+dy<N and 0<=x+dx<M:
            if array[y+dy][x+dx] == 0:
                clean_up(y+dy, x+dx, dd)
                break
    
    # 후진
    back = [(+1,0), (0,-1), (-1,0), (0,+1)]
    dy, dx = back[d]
    if array[y+dy][x+dx] != 1:    # 벽이 아니라면 후진
        clean_up(y+dy, x+dx, d)
    
    return 0

clean_up(r, c, d)
print(*array, sep='\n')
print(cnt)
    
    