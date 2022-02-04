from itertools import combinations
from collections import Counter

L, C = map(int, input().split())
alphabet = list(input().split())
alphabet.sort()

array = combinations(alphabet, L)
for x in array:
    count = Counter(x)
    if 1<= count['a']+count['e']+count['i']+count['o']+count['u']<L-1:
        print(''.join(x))

''' [review]
일반적인 사전과는 달리
Counter 객체는 존재하지 않는 키에 대해서도 조회 가능.
dict['없는키']는 에러가 나지만, count['없는키']는 0을 반환
'''
