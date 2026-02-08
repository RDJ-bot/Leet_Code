# Brute Force
s = "Lets take coffe"
ans = ""
ss = ""
for i in range(len(s)):
    if s[i] != " ":
        ss += s[i]
    else:
        ans += ss[::-1]+" "
        ss = ""
ans += ss[::-1]
print(ans)


# Better
s = "Lets take coffe"
arr = s.split(" ")
ans = ""

for i in arr:
    ans += i[::-1]+" "
print(ans.rstrip(" "))