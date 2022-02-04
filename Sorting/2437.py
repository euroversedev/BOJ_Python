N = int(input())
array = sorted(list(map(int, input().split())))
check = [True] + [False] * (100000)

for weight in array:
    # 기존에 가능했던 무게 + 추가된 weight = 새롭게 가능해진 무게
    idx = [weight]
    for i in range(1, len(check)):
        if check[i] == True and i + weight < len(check):
            idx.append(i+weight)
    
    for i in idx:
        check[i] = True
    
    if False in check[:weight]:
        break
print(check.index(False))
    