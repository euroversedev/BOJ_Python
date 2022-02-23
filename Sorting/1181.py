import sys
N = int(input())
array = list(set(list(sys.stdin.readline().strip() for _ in range(N))))
print(*sorted(array, key=lambda x:(len(x), x)), sep='\n')