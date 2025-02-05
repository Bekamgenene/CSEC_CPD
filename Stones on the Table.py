n = int(input())
colors = input()
sol = 0

for i in range(n - 1):
    if colors[i] == colors[i + 1]:
        sol += 1

print(sol)
