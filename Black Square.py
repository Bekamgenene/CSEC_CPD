a = list(map(int, input().split()))
s = input()
total = 0

for i in s:
    total += a[int(i) - 1]

print(total)
