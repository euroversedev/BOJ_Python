N = input()
len_N = len(N)

result = 0
for i in range(len_N):
    result += int(N)-((10**i)-1)
print(result)