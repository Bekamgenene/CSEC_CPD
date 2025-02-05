n = int(input())
events = list(map(int, input().split()))
hired = untreated = 0

for event in events:
    if event > 0:
        hired += event
    elif hired > 0:
        hired -= 1
    else:
        untreated += 1

print(untreated)
