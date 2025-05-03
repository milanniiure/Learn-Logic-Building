# Determine sum of a number until it becomes a single digit

def sumUntilSingle(num):
    while num >= 10:
        sum = 0
        while num > 0:
            digit = num % 10
            sum += digit
            num = num//10
        num = sum
    return num

number = int(input("Enter a number to check the sum until it becomes a single digit :"))
single = sumUntilSingle(number)
print(f"The sum of {number} digits becomes {single} as single digit.")