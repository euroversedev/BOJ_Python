import sys

n, m = map(int, sys.stdin.readline().strip().split())
data = list(map(int, sys.stdin.readline().strip().split())) +[0]

count = 0
interval_sum = 0
end = 0

# move 'start' pointer to the right.
for start in range(n):
    # move 'end' pointer to the right.
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # If the sum of interval is 'm', count the number.
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)