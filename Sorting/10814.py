import sys

N = int(input())
array = sorted(enumerate([tuple(sys.stdin.readline().strip().split()) for _ in range(N)])
              , key = lambda x: (int(x[1][0]), x[0]))

for idx, (age, name) in array:
    print(age, name)
