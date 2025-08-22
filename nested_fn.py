# def outer():
#     def inner():
#         print("Hello from inside")
#     inner() # calling inner from inside outer
# outer()   #calling outer object to print its inner function    



# def outer():
#     def inner(x):
#         print(x*x)
#     inner(3)
# outer() 





# # Closure or nested function
# def org():
#     def dup():
#         return n*2
#     n=3
#     return dup()
# print(org())



# # Encapsulation or object oriented encapsulation
# def outer(n):
#     def inner():
#         return n
#     return inner()
# print(outer("hello"))



# def x(n1, n2):
#     def y():
#         return n1+n2
#     print(y())
#     return n1*n2
# print(x(3,6))



# def a(n):
#     def b():
#         return f"from b {n+1}"
#     print(b())
#     return n
# print(a(9))



# def x(a, b):
#     def y():
#         return a+b
#     print(y())
#     print(a* b)
# x(3, 6)



# def big(*args, **ptrs):
#     print(sum(args), ptrs)
#     def small():
#         return sum(args)
#     print(small())
# big(1,2,3, name = "alice", age = 27)
