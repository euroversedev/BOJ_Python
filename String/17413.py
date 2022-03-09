import sys

S = sys.stdin.readline().strip()

stack = []
result = []
tag = False
for ch in S:
    if ch == '<':
        while stack:
            result.append(stack.pop())
        result.append('<')
        tag = True
        continue
    
    if ch == '>':
        result.append('>')
        tag = False
        continue
    
    if ch == ' ':
        while stack:
            result.append(stack.pop())
        result.append(' ')
        continue
        
    # 태그 내의 문자는 그냥 넣음
    if tag == True:
        result.append(ch)
        continue
    
    # 태그가 아닌 문자는 거꾸로 넣기 위해 스택에 저장
    if tag == False:
        stack.append(ch)

while stack:
    result.append(stack.pop())
print(''.join(result))