''' [ 이진 탐색 ]
1. 재귀 함수를 이용한 방법
2. 반복문을 이용한 방법
3. bisect 라이브러리를 이용한 방법
'''

''' 반복문을 이용한 방법은 주어진 상황에 따라 적절한 탐색법을 고수하는게 중요한듯.
가장 좋은 예시가 2110번인듯.
'''
# 1. mid = (start+end+1) //2로 하는 방법
start, end = 0, 10**9
while start < end:
    mid = (start+end+1) // 2
    # 인접 거리를 mid로 하여 공유기 설치가 가능한 경우 => 더 큰 mid를 알아본다.
    if func(mid):
        start = mid
    
    # 불가한 경우 => 더 작은 mid를 알아본다.
    else:
        end = mid -1
        
# 2. result변수로 답을 따로 저장해두는 방법
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