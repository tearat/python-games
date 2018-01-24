a = [[0.7] * 7 for i in range(7)] 
a = [[1,2,3,4,5,6,7] for i in range(7)]

for i in range(7): 
    for j in range(7): 
        print(a[i][j], "", end="") 
    print()
    
for m in range(1, 7):
    for n in range(1, 7):
        a[m][n] = a[7-m][n]
        
print()     
for i in range(7): 
    for j in range(7): 
        print(a[i][j], "", end="") 
    print()