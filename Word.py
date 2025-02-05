s = input()
lower_count = 0
upper_count = 0

for char in s:
    if char.islower():
        lower_count += 1
    else:
        upper_count += 1

if upper_count > lower_count:
    print(s.upper())
else:
    print(s.lower())
