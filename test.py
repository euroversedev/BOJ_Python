def solution(brown, yellow):
    answer = [0, 0]
    start = int(yellow**0.5)
    # i는 노란색의 가로 길이
    for i in range(start, yellow+1):
        if yellow % i == 0 and (yellow//i) <= i:
            j = yellow // i
            if 2*i + 2*(j+2) == brown:
                answer = [i+2, j+2]
            
    return answer

print(solution(3, 3))