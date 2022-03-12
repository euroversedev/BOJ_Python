import sys

T = int(input())
for _ in range(T):
    N = int(input())
    array = [0] + list(map(int, sys.stdin.readline().strip().split()))
    for i in range(1, N+1):
        array[i] += array[i-1]
    
    interval_sum = []
    for i in range(N+1):
        for j in range(0, i):
            interval_sum.append(array[i]-array[j])
    print(max(interval_sum))