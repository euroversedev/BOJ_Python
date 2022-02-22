import sys

N, M = map(int, input().split())
board = [list(sys.stdin.readline().strip()) for _ in range(N)]

chess = [list("BWBWBWBW"), list("WBWBWBWB")]
def check1(y, x):
    cnt = 0
    tmp = [chess[0], chess[1], chess[0], chess[1], chess[0], chess[1], chess[0], chess[1]]
    for i in range(8):
        for j in range(8):
            if board[y+i][x+j] != tmp[i][j]:
                cnt += 1
    return cnt

def check2(y, x):
    cnt = 0
    tmp = [chess[1], chess[0], chess[1], chess[0], chess[1], chess[0], chess[1], chess[0]]
    for i in range(8):
        for j in range(8):
            if board[y+i][x+j] != tmp[i][j]:
                cnt += 1
    return cnt


min_ = 10**9
for i in range(N-7):
    for j in range(M-7):
        min_ = min(min_, check1(i, j), check2(i, j))

print(min_)

''' [review] 
count 하는 방법이 옳지 못할 수도 있다.
흰색 32개, 검은색 32개라고해서 모두 체스 모양은 아니다.

틀린 코드:
        cnt = 0
        for y in range(8):
            for x in range(8):
                if board[i+y][j+x] == 'W':
                    cnt += 1
        print(cnt-32)

        min_ = min(min_, abs(cnt-32))
'''