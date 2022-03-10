import sys

N, C = map(int, sys.stdin.readline().strip().split())
array = sorted([int(sys.stdin.readline().strip()) for _ in range(N)])


# func는 그리디가 성립함
def func(distance):
    # cnt는 설치한 공유기 수
    cnt = 1
    a = array[0]
    for b in array[1:]:
        if b-a >= distance:
            a = b
            cnt += 1
        
        if cnt >= C:
            return True
    return False

start, end = 0, 10**9
while start <= end:
    mid = (start+end) // 2
    # 인접 거리를 mid로 하여 공유기 설치가 가능한 경우 => 더 큰 mid를 알아본다.
    if func(mid):
        start = mid+1
        result = mid
    
    # 불가한 경우 => 더 작은 mid를 알아본다.
    else:
        end = mid -1

print(result)