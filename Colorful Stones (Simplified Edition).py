s = input()
t = input()
j = 0
for i in t:
    if i == s[j]:
        j += 1
        if j == len(s):
            break
print(j + 1)
