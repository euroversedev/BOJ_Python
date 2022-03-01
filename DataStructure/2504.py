S = input()

S = S.replace('()', '2')
S = S.replace('[]', '3')
    
stack = []
for ch in S:
    if ch.isdigit():
        stack.append(ch)
    
    if ch == '(' or ch == '[':
        stack.append(ch)
        
    if ch == ')':
        sum_ = 0
        while stack and stack[-1].isdigit():
            sum_ += int(stack.pop())
        
        if stack and stack[-1] == '(':
            stack.pop()
            stack.append(str(sum_ * 2))
        
        else:
            stack.append(ch)
    
    if ch == ']':
        sum_ = 0
        while stack and stack[-1].isdigit():
            sum_ += int(stack.pop())
        
        if stack and stack[-1] == '[':
            stack.pop()
            stack.append(str(sum_ * 3))
        
        else:
            stack.append(ch)

try:
    print(sum(map(int, stack)))
except:
    print(0)

''' review
1. 문자열은 replace( ) 메소드를 지원한다.
2. 문자열의 숫자 판별은 isnum()이 아니고 isdigit()이다.
   알파벳은 isalpha()이다.

'''