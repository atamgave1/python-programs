n=int(input("Enter Number"))
a=list(map(int,str(n)))
b=list(map(lambda x:x**3,a))
if(sum(b)==n):
    print("Armstrong number")
else:
    print("Not an Armstrong number")
        
