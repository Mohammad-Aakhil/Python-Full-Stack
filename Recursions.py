# def x(n):
#     if (n == 0):
#         return    #Base case or stopping condition
#     print(n)
#     x(n-1)        #Recursive case
# x(5)

# print("")

# def even(n):
#     if n == 12:
#         return
#     print(n)
#     even(n+2)  #recursion
# even(2)

# print("")



# #factorial of a number
# def fact(n):
#     if (n == 0 or n==1):
#         return 1
#     return n * fact(n-1)
# print(fact(5))

# print("")



# #sum of n natural numbers
# def sum(n):
#     if n == 1:
#        return 1
#     return n+ sum(n-1)
# print(sum(5))
    
    

# def fact(n):
#     if (n == 0) or (n == 1):
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(5))




n = int(input("Enter value to print its value in fibinocci series :"))
def febn(n):
    if (n == 0) or (n == 1):
        return 1
    else:
        return febn(n-2) + febn(n-1)
print(f"The {n}th value in fibinooci series is {febn(n)}")    




