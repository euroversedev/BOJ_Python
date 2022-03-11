import sys

N = int(input())
array = list(map(int, sys.stdin.readline().strip().split()))

isPalindrome = [[False]* (N) for _ in range(N)]
for start in range(N):
    for end in range(N-1, -1, -1):
        if start <= end and isPalindrome[start][end]==False:  
            # start~end 수열의 팰린드롬 여부를 판단하고,
            # 팰린드롬인 경우 부분 수열을 모두 팰린드롬 처리해버리자
            flag = True
            i, j = start, end
            while i <= j:
                if array[i] == array[j]:
                    i, j = i+1, j-1
                    continue 
                else:
                    flag = False
                    break
                    
            # 팰린드롬이 맞으면,
            i, j = start, end
            if flag:
                while i <= j:
                    isPalindrome[i][j] = True
                    i, j = i+1, j-1
            
# print(*isPalindrome, sep='\n')

M = int(input())
for i in range(M):
    start, end = map(int, sys.stdin.readline().strip().split())
    print(int(isPalindrome[start-1][end-1]))