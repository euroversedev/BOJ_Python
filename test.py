import heapq

h = [(1,1),(2,2),(1,3),(1,2),(2,1)]
heapq.heapify(h)
print(h)

while h:
    print(heapq.heappop(h))