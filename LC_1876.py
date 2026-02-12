s = "aababcabc"        #4
s = "xyzzaz"           #1
count = 0

for i in range(len(s)-2):
    a = s[i]
    b = s[i+1]
    c = s[i+2]

    if a!=b and b!=c and c!=a:
        count += 1

print(count)