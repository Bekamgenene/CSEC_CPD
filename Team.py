n = int(input())  
result = sum(1 for _ in range(n) if input().split().count('1') >= 2)  
print(result)
