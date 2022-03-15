import sys
import heapq

N = int(sys.stdin.readline().strip())

max_heap = [(10001, 10001)]
min_heap = [(10001, 10001)]

max_heap_size = 0
min_heap_size = 0

for _ in range(N):
    num = int(sys.stdin.readline().strip())
    
    if num <= max_heap[0][1]:
        heapq.heappush(max_heap, (-1*num, num))
        max_heap_size += 1
    
    elif num > max_heap[0][1]:
        heapq.heappush(min_heap, (num, num))
        min_heap_size += 1
        
    if max_heap_size > min_heap_size + 1:
        key, value = heapq.heappop(max_heap)
        heapq.heappush(min_heap, (value, value))
        max_heap_size -= 1
        min_heap_size += 1
    
    if max_heap_size < min_heap_size:
        key, value = heapq.heappop(min_heap)
        heapq.heappush(max_heap, (-1*value, value))
        max_heap_size += 1
        min_heap_size -= 1
    

    print(max_heap[0][1])
