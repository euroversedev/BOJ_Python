import sys

s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()

hash_s1 = list(map(ord, s1))
sum_hash_s1 = sum(map(ord, s1[:len(s2)]))
sum_hash_s2 = sum(map(ord, s2))

while True:
    if sum_hash_s1


print(sum_hash_s2)

''' review
String Matching 문제이다.
KMP 혹은 Rabin-Karp(Rolling-Hash) 알고리즘을 사용할 수 있다.
위 코드는 Rabin-Karp를 이용한 풀이이다.

파이썬의 경우 in 연산자를 사용해도 되지만, 
조금만 변형되면 풀이에 어려움을 겪을 수 있으므로 잘 알아두자.
'''