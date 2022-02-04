import sys
import heapq

N = int(input())
array = list(map(int, sys.stdin.readline().split()))
heapq.heapify(array)

add = 0
total = 0
while array:
    MIN = heapq.heappop(array)
    add += MIN
    total += add
print(total)


''' [review]
heapq.heapify()는 기존 리스트를 힙으로 만들어주며,
반환값이 없기때문에 바로 사용하면 된다.

최소값 가져오기 위해 heap을 쓸수도 있지만
위와 같은 상황에서는 그냥 array.sort()가 더 용이했음.
'''