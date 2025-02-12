n = int(input())  
birds = list(map(int, input().split()))  
 
m = int(input())  
 
for _ in range(m):
    i, x = map(int, input().split())  
    i -= 1  
 
    if i > 0:
        birds[i - 1] += x - 1  
    
    if i < n - 1:
        birds[i + 1] += birds[i] - x  
    
    birds[i] = 0  
 
for b in birds:
    print(b)
