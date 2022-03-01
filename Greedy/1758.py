import sys

N = int(input())
tips = [int(sys.stdin.readline().strip()) for _ in range(N)]

result = 0
for idx, tip in enumerate(sorted(tips, reverse=True)):
    if tip > idx:
        result += tip - idx

print(result)