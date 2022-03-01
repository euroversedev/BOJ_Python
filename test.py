import heapq
h = [(1,2),(3,4),(3,3),(3,5),(4,7),(4,5),(4,1), (5,6),(5,4),(5,3)]
heapq.heapify(h)

while h:
    print(heapq.heappop(h))