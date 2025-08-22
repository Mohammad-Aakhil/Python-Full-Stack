def prt_nums(n):
    for i in range (n):
        print(i)
prt_nums(6)



def sum(n):
    count = 0
    for i in range(n):
        count +=i
    print(f"the sum of first {n-1} natural numbers is {count}")
sum(6)



def details(name, height, weight):
    return f"hello {name} you're weighing {weight}kgs standing at {height} feet tall"
print(details("Aakhil", "5'7", 57))



def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *=i
    print(f"the factorial of {n} is {fact}")
factorial(5)



def x(name, age, r_no):
    print(f"your name is: {name},you are {age} years old, your rollno is :{r_no}")
x("Alice", 27, 1234)



def s(age = 1, num = 11, name = "ali"):
    print(name, age, num)
    print (f"this is x val: {age} this is y_val {name} and this is z_val{num}")
s("alice", 24, 234)



def mix_sum(a,b,c):
    return (a+b+c), (a*b*c), (a-b-c)
print(mix_sum(3,6,8))
x = mix_sum(3,5,6)
for i in x:
    print(i)


    
def letter(*add):
    print(sum(add))
letter(1,2,3,4)



'''
*args takes multiple positional arguments
*args takes positional arguments as input gives as tuple
'''
def sum_numbers(*args):
    return sum(args)
print(sum_numbers(1, 2, 3))  # Output: 6



def details(**args):
    return args
print(details(x=1,y=2,z=3))


def details(**args):
    return args
print(details(name="alice", age=27, id=12345))



sum = lambda x,y :x+y
print(sum(3,6))


def add (x,y):
    print(f"x : {x}, and y : {y}")
    print(f"x+y = {x+y}")
add(y=5,x=10)
