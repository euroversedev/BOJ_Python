s = list(map(int, input()))

cnt_0 = 0
cnt_1 = 0
pre_num = -1

for ch in s:
    if ch != pre_num:
        if ch == 0:
            cnt_0 += 1
        if ch == 1:
            cnt_1 += 1
        pre_num = ch

print(min(cnt_0, cnt_1))
