s = input()

operator = []
num = []

n = 0
for i in range(len(s)):
    if s[i] == '+' or s[i] == '-':
        operator.append(s[i])
        num.append(n)
        n = 0
    
    else:
        n = n*10 + int(s[i])
num.append(n)

result = 0
if '-' in operator:
    for i in range(operator.index('-')+1):
        result += num[i]
    for j in range(operator.index('-')+1, len(num)):
        result -= num[j]
else:
    result = sum(num)
print(result)


''' [review]
리스트에서 특정 원소의 인덱스 가져오는 법
: idx = List.index(elem)

'-' 부호를 기준으로 나눌려고 복잡하게 인덱스 구해도 되지만,
array = s.split('-') 로 하면 - 부호를 기준으로 나누어짐.
'''