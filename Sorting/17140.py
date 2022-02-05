import sys
from collections import Counter
import copy

# A[r-1][c-1]이 k가 되기 위한 연산 횟수 구하기
r, c, k = map(int, input().split())   

A = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(3)]


# R 연산 : 행 >= 열
def func_R():
    global A
    
    for i, row in enumerate(A):    # 매 행마다
        count = Counter(row)
        del count[0] 
        li = sorted(count.most_common(), key = lambda x: (x[1], x[0]))
        li = list(sum(li, ()))
        row = li
        A[i] = row
        
    max_len = max(map(len, A))
    for i, row in enumerate(A):
        if len(row) < max_len:
            A[i] = row + [0] * (max_len-len(row))
        
        if len(row) > 100:
            A[i] = row[:100]
        
# C 연산 : 행 < 열
def func_C():
    global A
    A = [list(x) for x in zip(*A)]
    func_R()
    A = [list(x) for x in zip(*A)]

cnt = 0
while True:
    
    if cnt > 100:
        print(-1)
        break
        
    if len(A) >= r and len(A[0]) >= c:
        if A[r-1][c-1] == k:
            break
    
    cnt += 1
        
    flag = True
    if len(A[0]) <= len(A):
        func_R()
        flag = False
    
    if flag:
        func_C()
    
if cnt <= 100:
    print(cnt)


''' [review]
1. 이중 리스트 전치(transpose)하는 법
: transposed_array = [list(x) for x in zip(*array)]

2. A[r-1][c-1]에서 index runtime Error가 발생하는 경우가 있어서
범위 안에 속할 때만 검사하도록 했음
=> try & except 문으로 하면 간단함.
try:
    if A[r-1][c-1] == k:
        print(cnt)
        return
except:
    pass
    
3. 리스트 안의 모든 원소 삭제
array.clear()
'''