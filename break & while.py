for i in range(1,11):
    if i == 8:
        continue
    print(f"square of {i} is {i**i}")






# using break and continue while iterating through a list of strings
# list = ("aakhil", "pavan", "bhaskar", "satish")    
# i=0
# while i < len(list):
#     if list[i] == "bhaskar":
#         i+=1
#         continue
#     print(list[i])
#     i+=1



list = ("aakhil", "pavan", "bhaskar", "satish")    
i=0
while i < len(list):
    if list[i] == "bhaskar":
        # i+=1
        break
    print(list[i])
    i+=1
