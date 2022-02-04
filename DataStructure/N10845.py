N, K = map(int, input().split())

array = [i for i in range(1, N+1)]

result = []
while array:

    if len(array) > K:
        result.append(array[K-1])
        array = array[K:] + array[:K-1]
    else :
        result.append(array[(K-1)%len(array)])
        array = array[K%len(array):K%len(array) + len(array) - 1]
print("<"+', '.join(map(str,result))+">")