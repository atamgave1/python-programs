def printstmt(str):
    "This prints a passed string into this function"
    print(str)
    return

def printval(name,age):
    "Print value"
    print("Name:",name)
    print("Age:",age)
    return

def printdefaultval(name,age=50):
    "Print value"
    print("Name:",name)
    print("Age:",age)
    return

def prininfo(arg1,*var):
    "Print value"
    print(arg1)
    for v in var:
        print(v,end=" ")
    return

sum=lambda x,y:x+y
'''
printstmt("calling function")
printval(age=20,name="Python")
printdefaultval(name="Python",age=30)
printdefaultval(name="Python")
prininfo(10)
prininfo(20,30,40)
print("\nSUM:",sum(10,5))
'''
