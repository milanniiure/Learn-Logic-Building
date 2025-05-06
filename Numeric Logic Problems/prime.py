import math
def is_prime(n):
    if n<=1:
        return False # number <=1 are not prime
    
    for i in range(2,int(math.sqrt(n))+1): # looping numbers from 2 to n-1 // range(2, 5) means 2,3,4 thats why we didnt write range(2,n-1)
        if n % i == 0:   # checking divisibility, if remainder 0, even numbers can't be prime except number 2
            return False 
    
    return True  # if no divisor found then its a prime number

number = int(input("Enter a number to check if it is a prime number or not: "))  # user input

# call the function
if is_prime(number):
    print(f"{number} is a prime number.")
    
else:
    print(f"{number} is not a prime number")

