def factorial(n):
    if n==0:
        return 1
    return(n * factorial(n-1))
num=int(input("enter a number to find its factorial  value:"))
print("factorial of num is",factorial(num)) 

    
    
      