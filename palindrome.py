def isPalindrome(x: int) -> bool:
        res=0
        temp=x
        if(x<0):
            return False
        while(temp>0):
            rem=temp%10
            res=res*10+rem
            temp=temp//10
        if(res==x):
            return True
        else:
            return False

n=int(input("Enter number:"))
print(isPalindrome(n))
