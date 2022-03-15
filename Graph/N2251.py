import sys

# limit size, Upper Case
A, B, C = map(int, sys.stdin.readline().strip().split())
answer = set()

# backtracking
def dfs(a, b, c):    # now size, lower Case
    if a == 0: answer.add(c)
    
    