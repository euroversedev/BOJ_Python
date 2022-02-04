from collections import Counter

n = int(input())
data = [list(input()) for _ in range(n)]

count = Counter()
ans = 0

for d in data:
    for i in range(len(d)):
        count[d[-i-1]] += 1 * (10 ** i)

chr2num = {key: 9 - i for i, (key, _) in enumerate(count.most_common())}

for d in data:
    ans += int(''.join(str(chr2num[x]) for x in d))
print(ans)
