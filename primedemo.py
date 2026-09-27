n=int(input("Enter number to check.."))
flag=False

if n==1 or n==0:
    print(n,"is not a prime number")
elif n >1 :
    for i in range(2,n):
        if (n%i)==0:
            flag=True
            break
        if flag:
            print(n,"is not prime")
        else:
            print(n,"is prime")
            
