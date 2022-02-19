from collections import Counter

N = 1
for _ in range(3):
    N *= int(input()) 


cnt = Counter(str(N))
for i in range(10):
    if str(i) in cnt:
        print(cnt[str(i)])
    else: print(0)

''' [review]

Counter 함수 사용법 (=딕셔너리 사용법)
https://codechacha.com/ko/python-convert-dict-to-list/

기본적으로 Counter(list)는 사전 자료형인 Counter객체를 반환한다.
list(Counter(list))를 하면 키값들만 리스트로 저장된다.
(키, 원소)를 함께 리스트에 저장하려면 list(Counter(list).items())

Counter(list).most_common은 빈도수가 높은게 앞으로 오게해서 사전을 정렬함.


++++
문자열에서 원소 세기
cnt = string.count(elem)
'''