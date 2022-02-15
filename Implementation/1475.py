import math

N = input()
cnt = [0] * 10
for num in N:
    cnt[int(num)] += 1

cnt[6] = math.ceil((cnt[6] + cnt[9]) / 2)
del cnt[9]
print(max(cnt))

''' [review]
- 올림, 내림, 반올림

import math
올림 : math.ceil(x)
내림 : math.floor(x)
반올림 : round(x, digit)

* 이때 round 함수에 주의하자,
  앞자리가 짝수일때와 홀수일때 처리 방식이 다르다.
round(4.5) -> 4
round(3.5) -> 4
'''