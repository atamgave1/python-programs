'''n=int(input("Enter number"))
rev=str(n)[::-1]
print(rev)'''

n=int(input("Enter number"))
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)
    
    
