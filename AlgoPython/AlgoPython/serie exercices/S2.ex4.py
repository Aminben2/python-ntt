# triangle
for i in range(6):
    for j in range(i+1):
        print("*", end=" ")
    print()
print()

# upside down
for i in range(6):
    for j in range(i):
        print(" ", end=" ")
    for k in range(6, i, -1):
        print("*", end=" ")
    print()
print()

# caré
for i in range(5):
    for j in range(5):
        print('*', end=" ")
    print()
print()

# caré vide
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()
