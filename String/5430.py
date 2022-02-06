import sys

T = int(input())
for _ in range(T):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    array = sys.stdin.readline().strip()
    
    if len(array) == 2:
        array = []
    else:
        array = array[1:-1]
    if array:
        array = list(map(int, array.split(',')))
        
    left = 0
    right = 0
    direction = -1    # 음수: 왼쪽 삭제, 양수 : 오른쪽 삭제
    for func in p:
        if func == 'R':
            direction *= -1
        
        elif func == 'D':
            if direction == -1:
                left += 1
            elif direction == 1:
                right += 1
    
    if left + right > len(array):
        print("error")
    
    else:
        array = array[left : len(array)-right]
        if direction == 1:
            array.reverse()
        print('[', end="")
        if array:
            print(*array, sep=',', end="")
        print(']')

''' [review]
모든 p를 반복문으로 돌면서 처리하면 시간 복잡도가 너무 큼

1. R과 D의 갯수를 세어 한번에 처리하는 방식으로 해야하고.
2. 필요하다면 tru&except 구문도 써보자
====>  다 필요없고 문제를 효과적으로 해결하기위해 더 고민하자.

★ strip()에는 무시하고 싶은 문자를 인자로 넣어줄 수 있음
ex. s = input().lstrip('[').rstrip(']') 이런 식으로 왼쪽 오른쪽 모두 가능
strip()은 문자열의 양끝에서부터 괄호안의 인자들을 모두 제거해줌. default = 공백/엔터 등
'''