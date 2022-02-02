import sys
K = int(sys.stdin.readline())
stack = [0]
for _ in range(K):
    n = int(sys.stdin.readline())
    if n == 0: stack.pop()
    else: stack.append(n)
print(sum(stack))

''' [review]
K가 10만 이하의 수인데,
int(input())으로 구현하면 4052ms
int(sys.stdin.readline())으로 구현하면 112ms가 나온다.

생각보다 input()이 반복할 시에
시간을 많이 잡아먹는다. 참고하자
++++++++
append()함수보다
리스트를 먼저 초기화 한 후에, 인덱스로 접근하는 것이 조금 더 빠르다고 한다.
'''