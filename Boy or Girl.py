user_name = input()
distinct_count = len(set(user_name))

if distinct_count % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
