import math

def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    
    return True

def sum_of_primes_upto(num): 
    total = 0  #initialised variable with 0 at starting for later use
    for i in range(2,num+1):  # Range from 2 to num (num included) eg. range(2,6) = 2,3,4,5 
                                                #it doesnot include 6 so to include ending point we did num + 1
        if is_prime(i):
            total += i
    return total

# call the function
number = int(input("Enter a number: "))
prime_sum = sum_of_primes_upto(number)
print(f"{prime_sum} is the total sum of all primes upto {number}")


# STEPS:
# import math library for later calculations
# create a function with a paramter to find prime number first,     eg. def is_prime(num):
# check if number is less than or equal to 1, return False          eg. if num <= 1 return False
# for loop with range (start, end)                                  eg. for i in range(2, int(math.sqrt(num))+1)
# if condition to check (if num % i == 0) , if so return False      eg. if num % 1 == 0: return False
# return True

# create a function with a paramter for sum upto n                  eg. sum_upton(num):
# initialize total                                                  eg. total = 0
# for loop with range(start with 2, end with last num)              eg. for i in range(2, num+1):
# if condition for prime or not, cause only taking prime for sum    eg. if is_prime(i):
# add total and i                                                   eg. total = total + i
# return total

# Print total