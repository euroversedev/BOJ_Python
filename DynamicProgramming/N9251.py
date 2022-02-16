import sys

s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()

# s1이 더 짧아야 시간복잡도 줄음
if len(s1) > len(s2):
    s1, s2 = s2, s1
    
for ch in s2:
    
    
''' [review]
브루트포스가 고려되는 문제에서
이중 배열을 이용한 DP가 가능하다.
'''