n = int(input())
cubes = list(map(int, input().split()))
cubes.sort()
for cube in cubes:
    print(cube, end=" ")
