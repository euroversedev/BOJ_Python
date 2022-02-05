import sys

N = int(input())
serial = [sys.stdin.readline().strip() for _ in range(N)]

def func(x):
    sum = 0
    for i in range(len(x)):
        if ord('0')<= ord(x[i]) <= ord('9'):
            sum += int(x[i])
    return sum

serial.sort()
sorted_serial = sorted(serial, key = lambda x: func(x))
sorted2_serial = sorted(sorted_serial, key = lambda x: len(x))
print(*sorted2_serial, sep='\n')


''' [review]
정렬 우선 순위가 주어진 경우 위와 같이 역순으로 정렬해주면 된다.
++ sorted 함수의 키 옵션으로 lamda 함수를 사용할 때, 인자를 여러개 넣어줄 수도 있다.
ex. sorted(serial, key = lamda x: (len(x), sum(x), x))
튜플로 감싸줘야 함을 기억하자!
'''