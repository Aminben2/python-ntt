# n = 5
# for i in range(1, n + 1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# print()


# n = 5
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
# print()

# n = 5
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# print()


# n = 6
# for i in range(1,n+1):
#     j = n - i
#     while j > 0 :
#         print(" ",end=" ")
#         j-=1
    
#     for k in range(1,i*2):
#         print("*",end=" ")
#     print()


# n = 6
# i = 1
# while i <= n :
#     j = n - i
#     while j >= 1:
#         print("a",end="")
#         j -= 1
#     k = 1
#     while k <= i:
#         print("*", end="")
#         k += 1
#     i += 1
#     print()


# n = 20
# i = 1
# while i <= n :
#     j = n - i
#     while j >= 1:
#         print(" ",end="")
#         j -= 1
#     k = 1
#     while k <= i:
#         print("*", end=" ")
#         k += 1
#     i += 1
#     print()
# l = 1 
# while l <= n - 1 :  
#     for m in range(1,l+1):
#         print(" ",end="")
#     u = 1
#     while u <= n - l:
#         print("*", end=" ")
#         u += 1
#     l += 1
#     print()


# n = 4
# i = 1
# while i <= n:
#     if i == 1 or i == n :
#         for j in range(1,n+1):
#             print("*",end=" ")
#         print()
#     else :
#         print("*",end="")
#         for k in range(1,n):
#             print(" ",end=" ")
#         print("*",end="")
#         print()
#     i += 1



# n = 4
# for i in range(1, n + 1):

#     for j in range(1,n-i+1):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print(k,end=" ")
#     print()


n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ") if j % 2 else print("+",end=" ")
    print()


