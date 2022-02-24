import sys
sys.setrecursionlimit(10**9)

def find_parent(parent, x, target, deep):
    if (x == parent[x] or x == target) and deep != 0:
        return x
    else:
        parent[x] = find_parent(parent, parent[x], target, deep+1)
        return parent[x]

T = int(input())

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    parent = [0] + list(map(int, sys.stdin.readline().strip().split()))
    
    for i in range(1, N+1):
        if i == find_parent(parent, i, i, 0):
            pass
            
            
            
''' review 
싸이클 찾는 문제 같은데.. 음.. 잘안풀린다
1,2,3,4가 있을때
1에 대한 싸이클을 찾고나면 2,3,4의 부모가 전부 바껴서 얘네들은 사이클을 못도네..?

=> 걍 부모(선택된 학생)을 올라타가지고 cnt를 증가시켜 가면서
자기 자신으로 돌아오는 경우에는 cnt반환하도록 해야하나..
'''