N = int(input())

s = input()
cnt = 0
pre_ch = 'X'
for ch in s:
    if ch != pre_ch:
        cnt +=1
        pre_ch = ch

print(cnt//2 +1)