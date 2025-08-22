add = lambda x,y : x+y 
print(add(2,2))



# product = lambda x : x**2 #square of given number
# print(product(6))



# cube = lambda x : x**3  #cube of given number
# print(cube(9))



# s =[2,3,4,5]
# s1 =(4,5,6,7)
# square = list(map(lambda x : x**x, s))
# print(square) 
# Even_out = list(map(lambda y : y if y%2 ==0 else y+1, s1))
# print(Even_out)



# s = int(input("enter a number to print it's cube"))
# square = lambda s : s**3
# print(square(s)) 



# s = list(map  (int, input("enter a list of numbers").split() ))
# square = list( map (lambda s : s**3, s))
# print(square)



# s = (1,2,3,4,5,6)
# even = list(filter(lambda x : x%2 == 0, s))
# print(even)



# #whatever the values of list are it returns o for even and 1 for add numbers
# s = (11,24,33,4,5,6)
# even = list(map(lambda x : x%2 , s))
# print(even)



# #we gave comparision "==" operator it returns true if remainder 0 else false if remainder 1
# s = (1,2,3,4,5,6)
# even = list(map(lambda x : x%2 ==0, s))
# print(even)



# s = ("Apple", "Antman", "Batman", "Ironman")
# a = list(filter(lambda x : x.startswith("A"), s))
# print(a)



# s = (-1,-2,-3,0,2,3,4)
# whole_nums = list(filter(lambda x: x>=0, s))
# print(whole_nums)



# s = {'name' : "alice", 'age' : 27, 'ID' : "112234"}
# list(map(lambda x : print(x, end =","), s.items()) ) 


s = {'name' : "alice", 'age' : 27, 'ID' : "112234"}
list(map(lambda x : print(x, end =","), s) ) 



from functools import reduce
s = [1,2,3,4,5]
add = reduce(lambda x, y : x+y, s)
print(add)



# a = (1,2,3,4)
# b = [4,5,6,7]
# b.extend(a)
# print(b)