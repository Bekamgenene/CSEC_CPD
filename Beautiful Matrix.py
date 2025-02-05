matrix = []
for _ in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(5):
    if 1 in matrix[i]:
        x = i + 1
        y = matrix[i].index(1) + 1
        break

r, c = 3, 3
print(abs(x - r) + abs(y - c))
