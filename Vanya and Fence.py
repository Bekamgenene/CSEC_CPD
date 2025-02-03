ip = input().split(" ")
heights = input().split(" ")

width = 0

n = ip[0]
fence = ip[1]

for i in range(len(heights)):
    if int(heights[i]) > int(fence):
        width += 2
    else:
        width += 1

print(int(width))
