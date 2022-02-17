import sys

N, M = map(int, sys.stdin.readline().split())
array = [False] * 2 + [True] * (M-1)

def solution():
    for i in range(2, int(M**0.5)+1):
        if array[i]:
            #for j in range(2, (M//i)+1):
            #    array[i*j] = False

            for j in range(2*i, M+1, i):
                array[j] = False

    for i in range(N, M+1):
        if array[i]:
            print(i)

solution()

''' [review]
소수 문제는 항상 명심하자...
"1은 소수가 아니다."
테케 꼭 넣어보자.

약수의 성질을 이용하면 위처럼 제곱근까지만 검사하면 됨.
방법 1. import math // int(math.sqrt(x))
방법 2. int(x**0.5)

for문을 C언어 for(시작;조건;증감)처럼 사용하고 싶으면
range에 인자를 3개 넘겨주면 됨. range(시작, 끝, 보폭)

함수로 만들어서 호출하면 더 빠르네? 뭐지?

'''