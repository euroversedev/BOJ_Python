import sys
from collections import Counter

N = int(input())
array = [(sys.stdin.readline().strip().split())[0] for _ in range(N)]
for name, cnt in sorted(list(Counter(array).items()), key=lambda x:x[0], reverse=True):
    if cnt % 2 == 1:
        print(name)

''' [review] 
문자열을 사전 역순으로 정렬하려면 
 key=lambda x: -x[0] 가 아니라,    
 key=lambda x:x[0], reverse=True 로 해야한다.
 
 전자의 경우 bad operand type for unary -: 'str'오류 뜸
'''