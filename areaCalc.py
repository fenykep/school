import math
print(math.pi)

def cube():
    a=input("How big side?")
    A=6*a**2
    print(A)
    
def rect():
    a=input("How much A?")
    b=input("How many B?")
    A=a*b
    print(A)
    
def sphere():
    r=input("What is radius?")
    A=4*math.pi*r**2
    print(A)
    
def circle():
    r=input("What is radius?")
    A=math.pi*r**2
    print(A)

select=raw_input("What do you want to calculate?")
#[cube(k),circle(c),sphere(s),rectangle(r)]
if(select=='k'):
    cube()
elif(select=='c'):
    circle()
elif(select=='s'):
    sphere()
elif(select=='r'):
    rect()
else:
    print("Sorry, no such thing yet.")
