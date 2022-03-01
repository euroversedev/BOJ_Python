import sys

i = 1
while True:
    S = sys.stdin.readline().strip()
    
    if '-' in S:
        break
    
    stack = []
    result = 0
    for ch in S:
        if ch == '{':
            stack.append('{')
        
        if ch == '}':
            # 스택이 비어있는 경우
            if not stack:
                result += 1
                stack.append('{')
                continue
            # 스택에 원소가 존재하는 경우
            if stack:
                stack.pop()
    
    # 스택에 원소가 남아 있는 경우
    if stack:
        result += len(stack) // 2

    print(f"{i}. {result}")
    i += 1