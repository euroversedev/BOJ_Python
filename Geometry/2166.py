import sys
N = int(input())

# 좌표
coordinates = [tuple(map(int, sys.stdin.readline().strip().split()))\
              for _ in range(N)]

# 외적 구하기 : 신발끈 공식
def outer(coordinates):
    coordinates += [coordinates[0]]
    plus = 0
    minus = 0
    for i in range(len(coordinates)-1):
        plus += coordinates[i][0] * coordinates[i+1][1]
        minus += coordinates[i+1][0] * coordinates[i][1]
    
    return plus - minus

result = abs(1/2*outer(coordinates))
print(result)

''' [review]
다각형의 넓이 구하기

방법 1. 삼각형 여러래로 나누기
다각형은 여러개의 삼각형으로 나눌 수 있다.

방법 2. 사선(신발끈) 공식
다각형의 넓이 = |(1/2) * 외적|

참고 URL :
https://ko.wikihow.com/%EB%8B%A4%EA%B0%81%ED%98%95-%EB%84%93%EC%9D%B4-%EA%B5%AC%ED%95%98%EA%B8%B0
https://gaussian37.github.io/math-algorithm-polygon_area/


++ 소수점 출력하기
1. round(x, 1) : x를 소수 두번째 자리에서 반올림함.
2. f-string
'''