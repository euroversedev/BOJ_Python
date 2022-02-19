import sys

_ = input()
A = set(list(map(int, sys.stdin.readline().strip().split())))
B = set(list(map(int, sys.stdin.readline().strip().split())))

C = A.union(B)
print(len(C))

''' [review]
교집합 set1 & set2    (set1.intersection(set2))
합집합 set1 | set2    (set1.union(set2))
차집합 set1 - set2    (set1.defference(set2))
대칭 차집합 set1 ^ set2
'''