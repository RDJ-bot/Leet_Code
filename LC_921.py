s = "()))(("

open_parenthesis = 0
ans = 0

for i in s:
    if i == "(":
        open_parenthesis += 1
    else:
        if open_parenthesis > 0:
            open_parenthesis -= 1
        else:
            ans += 1

print(open_parenthesis + ans)