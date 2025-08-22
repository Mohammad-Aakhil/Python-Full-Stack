D1 = {'name' : "Alice", 'age' : 27, 'ID' : 2345}

# print(D1['name']) #accessing value through key //raise error if key not present in the dict

# D1["age"] = 21  #updating value of a key
# print(D1)

# D1["country"] = "Brazil"  #adding new item/key:value pair
# print(D1)

# print(D1.keys()) #prints all keys in dict

# print(D1.values()) #prints all values in dict

# print(D1.items()) #prints all items in dict

# print(D1.pop('age')) #removes item by taking key as argument
# print(D1)

# D1.clear() #clears all items from  dict
# print(D1)

# print(D1.get('age')) #gets the value by key //does'nt raise the error if key not in the dict



#comprehensive dictionary 

# my_dict = {'x' : x*2 for x in range(1, 6)}
# print(my_dict)



# out of box/
# dc = {X :i+1 for i in range(1, 5)  for X in ['a','b','c','d','f']}
# print(dc)


dc = {k: v for k, v in zip(['a', 'b', 'c', 'd', 'f'], range(1, 6))}
print(dc)

dc = {k: v for k, v in zip(['Name', 'Age', 'ID', 'Country', 'Place', "Work place", "liability"], ["Shabbir", 27, 1234, "USA", "Austin, Texas", "Solutions Limited", "Tesla Car"])}
print(dc)
