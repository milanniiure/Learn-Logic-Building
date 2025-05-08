# Calculate the modular exponentiation and see how it works

def modularExp(base, exponent, modulus):
    result = 1
    base = base % modulus

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base)% modulus
        base = (base*base) % modulus
        exponent = exponent // 2
    return result

# user input
baseNumber = int(input("Enter the base number: "))
exponentNumber = int(input("Enter the exponent number: "))
modulusNumber = int(input("Enter the modulus number: "))
answer = modularExp(baseNumber, exponentNumber, modulusNumber)

print(f"Modular exponentiation of ({baseNumber}**{exponentNumber}) % {modulusNumber} is {answer}")