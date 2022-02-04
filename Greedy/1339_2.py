import sys
from collections import Counter

N = int(input())
words = [sys.stdin.readline().strip() for _ in range(N)]

count = Counter()
for word in words:    # 매 단어 word
    for i, ch in enumerate(word[::-1]):    # 매 글자 ch
        print(i, ch)
        count[ch] += 10**i

# 각 알파벳과 점수(랭크) 매칭
chr2num = {key: 9 - i for i, (key, _) in enumerate(count.most_common())}

result = 0
for word in words:
    # 각 단어를 숫자로 치환
    result += int(''.join(str(chr2num[ch]) for ch in word))
    
print(result)

""" [review]
Counter 함수로 단순히 각 알파벳의 등장횟수를 세는 것은 의미없음
=> 단위에 따라 차등 적용해야 함. ex. "ABC의 A"와 "AD의 A"는 다르다. 

차등 적용된 밸류를 저장하기 위해 사전 자료형을 사용했고,
most_common을 사용하기 위해 counter로 사전 자료형을 만들었음.

1. Counter() 함수
count = Counter(list or string.. Iterable) : {(원소:등장횟수)..}와 같이 사전 자료형 반환
count = Counter() : 단순히 사전 자료형 반환, "count['원소'] = 등장횟수"로 데이터 추가
count.most_common() : 등장횟수가 많은 순으로 정렬된 배열을 리턴 ex. [('A', 3), ('B', 2)..]

2. enumerate(Iterable) 내장 함수
: 인덱스와 원소를 튜플 형태로 반환하는 함수임.
for idx, elem in enumerate(['A', 'B', 'C']):
    print(idx, elem)

0 A
1 B
2 C

위 두 함수를 이용해 알파벳과 점수를 매칭했음.
count.most_common() => 등장횟수가 많은 순으로 정렬된 배열 반환
enumerate() => (순위, (key, 등장횟수)) 이런 식으로 반환됨

3. for문에서 문자열을 거꾸로 훑는법
array[::-1] => 문자열을 뒤집은 결과를 반환한다.
array[3:0:-1] => 3번부터 1번까지 역순 
"""