import sys

dic_ = {'+':1, '-':1, '*':2, '/':2, '(':3, ')':3}
S = sys.stdin.readline().strip()

result = []
stack = []
for ch in S:
    if ch.isalpha():
        result.append(ch)
        continue
        
    if not stack:
        stack.append(ch)
        continue
    
    while stack and dic_[stack[-1]] <= dic_[ch]:
        result.append(stack.pop())
    stack.append(ch)
    
print(result, stack)
    
    
        