# tup = (12,24,36,48,36,60,36)

# print(tup[1]) #prints index number of given value

# print(tup.index(36)) #prints index of given item

# print(tup.count(36)) #returns no of occurance of given item


#unpacking tuple
# a,b,c,d,e,f,g = tup
# print(a,b,c)

'''
comprehensions in tuple by wraping list
#In Python, tuple comprehensions don’t exist by design because 
# tuples are immutable and comprehension syntax implies dynamic 
# generation of items
'''
tup = ([x*2 for x in range (1, 11)])
print(tup)

tuple_o =tuple(tup)
print(tuple_o)


# tup = ({1,2,3,4})
# tup.clear
# print(tup)






