import sys
import heapq
from collections import defaultdict

dic = defaultdict(list)
minH = []    # (난이도, 문제번호) 저장
maxH = []

N = int(input())
for idx in range(N):
    key, value = map(int, sys.stdin.readline().strip().split())
    heapq.heappush(minH, (value, key))
    heapq.heappush(maxH, (-1*value, -1*key))
    dic[key].append(value)

    
M = int(input())
for _ in range(M):

    s = sys.stdin.readline().strip()
    
    if 'recommend' in s:
        # 가장 어려운 문제 출력, 문제 번호 큰 것
        if s[-2:] == ' 1':
            while maxH:
                a, b = heapq.heappop(maxH)
                if -1*a in dic[-1*b]:
                    print(-1*b)
                    heapq.heappush(maxH, (a, b))
                    break            
        
        # 가장 쉬운 문제 출력, 문제 번호 작은 것
        if s[-2:] == '-1':
            while minH:
                a, b = heapq.heappop(minH)
                if a in dic[b]:
                    print(b)
                    heapq.heappush(minH, (a, b))
                    break
        
    if 'add' in s:
        _, key, value = s.split()
        key, value = int(key), int(value)
        heapq.heappush(minH, (value, key))
        heapq.heappush(maxH, (-1*value, -1*key))
        dic[key].append(value)
    
    if 'solved' in s:
        _, key = s.split()
        key = int(key)
        del dic[key]