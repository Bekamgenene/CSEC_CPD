n = int(input())
home_teams = []
guest_teams = []

for _ in range(n):
    home, guest = map(int, input().split())
    home_teams.append(home)
    guest_teams.append(guest)

conflict_count = 0

for i in range(n):
    for j in range(n):
        if i != j and home_teams[i] == guest_teams[j]:
            conflict_count += 1

print(conflict_count)
