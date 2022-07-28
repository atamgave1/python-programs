n=int(input("Enter number\n"))
a=0
b=1
if(n<0):
    print("Incorrect Number")
else:
    print(a,b,end=' ')
    for x in range(2,n):
        c=a+b
        a=b
        b=c
        print(c,end=' ')
