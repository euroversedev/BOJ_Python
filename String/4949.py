import sys

while True:
    s = sys.stdin.readline().rstrip()
    
    # 종료 조건
    if s == ".":
        break
    
    stack = []
    for ch in s:
        if ch =='(' or ch =='[':
            stack.append(ch)
        
        if ch == ']' :
            if stack and stack[-1] == '[':
                stack.pop()
            
            else:
                stack.append(ch)
                continue
            
        
        if ch == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            
            else:
                stack.append(ch)
        
    if stack: print("no")
    else: print("yes")

        
''' review
"] [ ]"와 같이 ]가 단독으로 들어오는 경우에도 stack에 넣어줘야함을 잊지말자
'''