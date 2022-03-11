import sys

N = int(input())
array = [int(sys.stdin.readline().strip()) for _ in range(N)]
result = 0

# 양수 모음
positive = sorted([i for i in array if i > 0])
while positive:
    a = positive.pop()
    if positive:
        b = positive.pop()
        if a * b > a + b:
            result += a * b
        else:
            result += a + b
        continue
    
    result += a
        
    
# 음수 모음 + 0
negative = sorted([j for j in array if j <= 0], reverse=True)
while negative:
    a = negative.pop()
    if negative:
        b = negative.pop()
        if a * b > a + b:
            result += a * b
        else:
            result += a + b
        continue
    
    result += a
    
print(result)