s = input()
t = 0
prev = ord('a')

for i in s:
    diff = abs(ord(i) - prev)
    t += min(diff, 26 - diff)
    prev = ord(i)

print(t)
