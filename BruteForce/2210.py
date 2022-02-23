import sys
sys.setrecursionlimit(10**9)

board = [list(map(int, sys.stdin.readline().strip().split()))
        for _ in range(5)]


set_ = set()
move = [(1,0),(0,1),(0,-1),(-1,0)]
def dfs(y, x, num, len_):
    num = num*10 + board[y][x]
    len_ += 1
    if len_ == 6:
        set_.add(num)
        return
    
    for dy, dx in move:
        if 0<=y+dy<5 and 0<=x+dx<5:
                dfs(y+dy,x+dx,num, len_)
            
for i in range(5):
    for j in range(5):
        dfs(i, j, 0, 0)
        
print(len(set_))