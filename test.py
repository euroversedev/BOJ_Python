import heapq
h = [1,2,3,4,5,2,6,7,8,95,42,5,8,1,4]
heapq.heapify(h)
print(heapq.nsmallest(5, h))