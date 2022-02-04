import sys

N = int(input())
alphabet = []
rank = [0] * 10
for _ in range(N):    # 매 단어마다
    s = sys.stdin.readline().strip()
    step = 1
    for i in range(len(s)-1, -1, -1):    # 역순
        
        if s[i] not in alphabet:    # 없는 경우에는 추가한다.
            alphabet.append(s[i])
        
        idx = alphabet.index(s[i])
        rank[idx] += step
        step *= 10

rank2 = rank.copy()
# 순위에 따라 알파벳에 숫자부여
num = [0] * 10
for i in range(len(alphabet)):
    MAX = max(rank)
    idx = rank.index(MAX)
    num[idx] = 9-i
    rank[idx] = 0


result = 0
for i in range(10):
    result += num[i] * rank2[i]

print(result)

''' [review]
위 코드는 시간, 공간 복잡도는 적절하지만
코드가 매끄럽지 못하고 생각나는대로 한거라 코테에서 구현하기 어려울 듯함.

보완을 위한 솔루션 몇가지..
1. 등장횟수를 사전으로 만들어주는 함수 Counter
from collections import Counter
count = Counter(['A', 'B', 'C', 'A'])    // 리스트나 문자열이 인자로 옴
print(count['A'])    => 2 출력

1339_2에서 개선된 코드 확인하기
'''