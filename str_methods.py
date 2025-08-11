# #capitalize() -changes 1st letter of the string to capital letter
# S = "aakhil"
# print(S.capitalize())



# #find() - returns index value of the 1st letter of 1st occurance
# s = "cat on the wall"
# print(s.find("on"))



# #replace() -replaces old string with old string
# s = "Aakhil"
# print(s.replace("Aakhil","Mohammad"))
 


# #strip() -removes whitspaces/spaces, from before and after the start of the string.
# strip() also takes an argument as [strip(" ")] which is a blank by default, we can give 
#any character of our choice as argument which is present in the string we want to eliminate/remove 
#from the given string such as print(var.strip("_").
#it can take maximum of only 1 values as arguments/parameters

#Example_1 :-removing spaces from the original string by defalut

# s = """    _    _hello, world, i,m learning 
# python full stack"""
# print(s)
# print(" ")
# print(s.strip())

# Example_2
# s = "**hello_World**"
# c = s.strip("*")
# print(s)
# print(" ")
# print(c)



# split() -by default it takes "splitter" as "," and "step"
s= "ironman,thor,xcaptain"
print(s)
print(s.split(","))



#join()
# l = ["cat", "dog", "mouse"]
# print("_".join(l))
# print(l)



# # isalpha()
# s= "abcde"
# t= "abc123"
# print(s.isalpha()) #true
# print(t.isalpha()) #false



# # isdigit()
# s= "abcde"
# t= "123"
# print(s.isdigit()) #false
# print(t.isdigit()) #true



# # isalnum()
# s= "abcd1234"
# t= "abcd"
# print(s.isalnum()) #true
# print(t.isalnum()) #false



# # isspace()
# s="    i    "
# t="    "
# print(s.isspace()) #false
# print(t.isspace()) #true



