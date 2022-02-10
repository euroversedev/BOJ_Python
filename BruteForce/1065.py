N = int(input())

cnt = 0
for i in range(1, N+1):
    flag = True
    li_ = list(map(int, str(i)))
    diff = 0
    if len(li_) > 1:
        diff = li_[1] - li_[0]
    for j in range(1, len(li_)):
        if li_[j] - li_[j-1] != diff:
            flag = False
            break
    if flag: cnt += 1

print(cnt)