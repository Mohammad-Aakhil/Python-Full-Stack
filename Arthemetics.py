a = 12
b = 99

def add(x,y):
    print(x+y)

def sub(x,y):
    print(x-y)

def mult(x,y):
    print(x*y)

def D_rem(x,y):
    print(x%y)

def D_quo(x,y):
    print(x/y)

def D_floor_quo(x,y):
    print(x//y)

def powersRp2Lp(x, y):
    print(x**y)

def Half_a_num(x):
    print(x/2)

def Double_a_number(x):
    print(x*2)

def multiply_me_with_me(x):
    print(x*x)

def QR(x,y):
    def Q():
        print(x/y)
    def R():
        print(x%y)
    print(f"quotient is :{Q()}, remainder is :{R()}")

