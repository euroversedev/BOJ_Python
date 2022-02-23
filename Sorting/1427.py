N = input()
array = sorted(list(map(int, str(N))), reverse=True)
print(''.join(list(map(str,array))))