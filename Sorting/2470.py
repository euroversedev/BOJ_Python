N = int(input())
array = list(map(int, input().split()))

sorted_array = sorted(array, key=abs)
MIN = 2*(10**9)
result = (0, 0)
for i in range(N-1):
    if abs(sorted_array[i]+sorted_array[i+1]) < MIN:
        MIN = abs(sorted_array[i]+sorted_array[i+1])
        result = (i, i+1)

if sorted_array[result[0]] < sorted_array[result[1]]:
    print(sorted_array[result[0]], sorted_array[result[1]])
else:
    print(sorted_array[result[1]], sorted_array[result[0]])

''' [review]
리스트 절대값으로 정렬하기
=> sorted 함수의 key 옵션 활용, 함수를 인자로 사용
sorted_array = sorted(array, key = abs) 
++ abs는 절댓값 함수이다.

sorted_li = sorted(li, key = lamba x : round(x)) 이렇게도 가능
'''