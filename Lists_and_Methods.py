L1 = [11,22,33,44,55,66,33]

# print( L1[2] ) #printing value from list through it's index

# print(L2)  #printing item of the list using it's index number

# print(L1.index(44))  #prints index number of item '44'

# print(L1.append(72))  #add 72 to list at end

# print(L1.remove(11)) #removes given value from the list

# print(L1.pop()) #by default removes last item from list

# print(L1.count(33)) #prints no of accurances of given item

# print(L1.clear()) #clears all the items from the list

# print(L1)



# comprehensive list creation
multiply_same = [x*x for x in range(1,11)]
print(multiply_same)


step_even = [x+x for x in range(1,21,2)]
print(step_even)


s = ["_" if i%2 ==0 else i for i in range(1,11)]  #pavan's logic
print(s)


y = [x if x%2 !=0 else "_" for x in range(1,11)]  #my logic
print(y)


