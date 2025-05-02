# how does this work?
# A trailing zero is formed by multiplication of 5 and 2. so if we consider all prime factors of all numbers from 1 to n
# there would be more 2s than 5s. so the number of 0s is limited by number of 5s. If we count the number of 5s in prime
# factors, we get the result. 
# Example: 
# n=5 and 5! (5*4*3*2*1) has one 5 and three 2s (5*2*2*3*2*1). So the count of trailing 0s is min(1,3) = 1
# n=11 and 11! (11*10*9*8*7*6*5*4*3*2*1) has (11*5*2*3*3*2*2*2*7*2*3*5*2*2*3*2*1) has two 5s and eight 2s. 
# so the count of trailing 0 is min(8, 2) = 2

# we can observe that the number of 2s in prime factors is always more than or equal to the number of 5s. so we are
# counting 5s and we are done.


#      SO HOW TO CALCULATE NOW 
# Trailing 0s in n! = Count of 5s in prime factors of n! = floor(n/5) + floor(n/25) + floor(n/125)+ .. 
# until n//5^k is 0.


def count_trailing_zeros(n):
    count = 0
    i = 5

    while n//i > 0:
        count = count + n//i
        i = i*5
    
    return count

number = int(input("Enter a number to determine trailing zeros in the factorial of the number:"))
zeros = count_trailing_zeros(number)
print(f"{zeros} trailing zeros appeared in the {number}!")