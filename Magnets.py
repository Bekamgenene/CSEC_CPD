magnets = int(input())
count = 1
previous = input()

for _ in range(magnets - 1):
    current = input()
    if current != previous:
        count += 1
        previous = current

print(count)
