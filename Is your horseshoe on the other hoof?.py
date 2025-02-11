n = list(input().split())
l = []
for i in n:
    if i not in l:
        l.append(i)
print(len(n)-len(l))
