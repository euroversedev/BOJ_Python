N = int(input())

array = [[True] * N for _ in range(N)]    # 체스 말을 둘 수 있는 경우 True

hash_set_y = set()    # y축 해시셋
hash_set_x = set()    # x축 해시셋
hash_set_d1 = set()   # 대각선(diagnoal) 해시셋 x-y
hash_set_d2 = set()   # x+y

# backtracking
def dfs(board, y, x):

    # 가로 세로에 겹치는 퀸이 있으면 안됨.
    if y in hash_set_y or x in hash_set_x:
        return 0
    
    # 대각선에 겹치는 퀸이 있으면 안됨.
    if x-y in hash_set_d1 or x+y in hash_set_d2:
        return 0
    
    # 종료 조건
    if y == N-1:
        return 1

    hash_set_y.add(y)
    hash_set_x.add(x)
    hash_set_d1.add(x-y)
    hash_set_d2.add(x+y)
    
    sum_ = 0
    for next_x in range(N):
        sum_ += dfs(board, y+1, next_x)
        
    hash_set_y.remove(y)
    hash_set_x.remove(x)
    hash_set_d1.remove(x-y)
    hash_set_d2.remove(x+y)
                    
    return sum_

result = 0
for i in range(N):
    result += dfs(array, 0, i)
print(result)
                    
                        
''' N-Queen
https://youtu.be/gcuZ_VGIcn4
'''                