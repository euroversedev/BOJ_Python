import sys
sys.setrecursionlimit(10**9)

board = [list(map(int, sys.stdin.readline().strip().split()))
        for _ in range(5)]
visit = [[[] for _ in range(5)] for _ in range(5)]
print(visit)
set_ = set()
move = [(1,0),(0,1),(0,-1),(-1,0)]
def dfs(y, x, num, len_):
    num = num*10 + board[y][x]
    len_ += 1
    visit[y][x].append(len_)
    if len_ == 6: set_.add(num)
    
    for dy, dx in move:
        if 0<=y+dy<5 and 0<=x+dx<5:
            if len(str(num)) not in visit[y+dy][x+dx]:
                dfs(y+dy,x+dx,num, len_+1)
            
for i in range(5):
    for j in range(5):
        dfs(i, j, 0, 0)
        
print(len(set))