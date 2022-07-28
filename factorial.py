n=int(input("Enter number\n"))
fact=1
if(n==1):
    print(n)
else:
    for i in range(1,n+1):
        fact=fact*i
    print("factorial of {} is {}".format(n,fact))
          
    
