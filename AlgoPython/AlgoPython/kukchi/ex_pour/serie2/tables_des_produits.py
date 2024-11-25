print("X*Y\tI\t", end="")
for x in range(11):
     print(x, end="\t") 
print()

for x in range(11):
     print("---------", end="") 
print()

for y in range(11):
     print(f'{y}\tI', end="\t")
     for x in range(11):  
          print(f'{x*y}', end="\t")
     print()
      