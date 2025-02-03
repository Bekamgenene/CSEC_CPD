g = int(input())
s = input()

c = s.count('A') - s.count('D')

if c == 0:
    print('Friendship')
elif c > 0:
    print('Anton')
else:
    print('Danik')
