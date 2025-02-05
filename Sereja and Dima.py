cards = int(input())
nums = list(map(int, input().split()))

s, d = 0, 0
l, r = 0, cards - 1
s_turn = True

while l <= r:
    if nums[l] > nums[r]:
        chosen = nums[l]
        l += 1
    else:
        chosen = nums[r]
        r -= 1

    if s_turn:
        s += chosen
    else:
        d += chosen

    s_turn = not s_turn

print(s, d)
