import sys

N = int(sys.stdin.readline().strip())
data = [list(map(int, sys.stdin.readline().strip().split()))
       for _ in range(N)]

sorted_data = sorted(data, key = lambda x : (x[0], x[1]))
dp = [0] * (max(end for start, end in sorted_data)+1)
for i in range(0, len(sorted_data)):
    start, end = sorted_data[i]
    dp[end] = max(*dp[:end+1], dp[start]+1)

print(sorted_data)
print(dp)
print(dp[-1])
    


                     