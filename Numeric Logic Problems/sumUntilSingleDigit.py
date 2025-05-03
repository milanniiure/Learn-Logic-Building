# Determine sum of a number until it becomes a single digit



def sumUntilSingle(num):
    while num >= 10:            # once num > 10, it automatically becomes single digit, no need to add
        sum = 0         # for initial start, and to reset. If we didn't it will take value of sum+digit which is in while loop
        while num > 0:         # num should be greater than zero to keep adding, once num becomes zero, loop stops
            digit = num % 10   # we did modulus with 10 because every number is represented in base 10 format or 
                                # decimal number, eg. 432 % 10 = 3
            sum += digit       # the remaining number is stored in digit variable, and we ve to keep adding number until it becomes zero
                                # so initial or later madeup sum + remaining digit will be stored in sum variable
            num = num//10      # it removes last digit of number, eg. 432 // 10 = 43, 43 became next number
        num = sum              # after loop breaks a number into digits and add them all, num = sum is of outer while loop,
                                # and num has 0 in outer loop initially and later we stored sum into num
    return num

number = int(input("Enter a number to check the sum until it becomes a single digit: "))
single = sumUntilSingle(number)
print(f"The sum of {number} digits becomes {single} as single digit.")


# Example: 432
# digit = num % 10 [ 432 % 10 = 2 ] 2 is stored in digit variable
# sum = sum + digit [ 0 + 2 = 2 ] initially sum was started with 0, so 2 is stored in sum variable
# num = num // 10 [ 432 // 10 = 43 ] 43 is stored in num variable
# Loop continues until num > 0, as of now num has 43
# 
# again,
# digit = num % 10 [ 43 % 10 = 3 ] 3 is stored in digit variable
# sum = sum + digit [ 2 + 3 = 5 ] 5 is stored in digit variable
# num =  num // 10 [ 43 // 10 = 4 ] 4 is stored in num variable
# 
# again, because num is still greater than 0
# digit = num % 10 [ 4 % 10 = 4] 4 is stored in digit variable
# sum = sum + digit [ 5 + 4 = 9] 9 is stored in sum variable
# num = num // 10 [ 4 // 10 = 0] 0 is stored in num variable

# now, num = 0, Inner while loop stops, because to continue loop (num > 0) was the condition
# now outer loop is still on, num = sum [ num = 9] in outer loop
# outer loop also stops cause, it has condition num should be greater than or equal to 10 