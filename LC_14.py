strs = ["flower","flow","flight"]

min_len = float('inf')
i = 0
ans = 0
for s in strs:
    if len(s) < min_len:
        min_len = len(s)

while i < min_len:
    for s in strs:
        if s[i] != strs[0][i]:
            ans = strs[0][:i]
            print(ans)
            exit()
    i += 1

ans = strs[0][:i]
print(ans)
