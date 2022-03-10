import sys

''' 
bisect를 사용하지 않은 방법
'''
N, M = map(int, sys.stdin.readline().strip().split())

titles = []
values = []
for _ in range(N):
    title, value = sys.stdin.readline().strip().split()
    titles.append(title)
    values.append(int(value))

def binary_search(start, end, target):
    if start > end:
        return start
    
    mid = (start+end)//2
    
    if values[mid] < target:
        return binary_search(mid+1, end, target)
    
    if values[mid] >= target:
        return binary_search(start, mid-1, target)
    
    
for _ in range(M):
    target = int(sys.stdin.readline().strip())
    # idx = binary_search(0, N-1, target)
    
    start, end = 0, N-1
    while start <= end:
        mid = (start+end)//2
        
        if values[mid] < target:
            start = mid+1
        
        if values[mid] >= target:
            end = mid-1
    
    print(titles[start])