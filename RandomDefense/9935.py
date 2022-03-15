import sys

S = sys.stdin.readline().strip()
bomb = list(sys.stdin.readline().strip())

len_bomb = len(bomb)

stack = []
for ch in S:
    stack.append(ch)
    
    try:
        if stack[-len_bomb:] == bomb:
            del stack[-len_bomb:]
    except:
        continue

print(''.join(stack) if stack else "FRULA")


# while True:
#     pre_len = len(S)
#     S = S.replace(bomb, "")
#     post_len = len(S)
    
#     if pre_len == post_len:
#         break
        
# print(S if S else "FRULA")