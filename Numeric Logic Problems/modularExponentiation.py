# solve the modular Exponentiation efficiently ( Used in cryptography, competitive programming, modular arthmetic

# Modular Exponentiation : Naive approach:
# Answer : (a power b modulus c) 3^13 % 7 
# (3^13%7 = 1594323 % 7, its inefficient)

# Efficient Method: Square and Multiply Method (Binary Exponentiation)
# convert expoenent to binary (to check bits)
# initialize result with 1
# square the result, do mod and store it on result
# multiply the result by base (if bit is 1) otherwise skip multiplication part , do mod and store it on result var
# after processing all bits final answer will be result var

# Example:
# 7^5 % 9   (a power b mod c)
# result has 1 as starting value
# to know bits : 5 = 101 (convert exponent into binary)

# SQUARE: 1**2 % 9 = 1         (result X power mod c )
# MULTIPLY : 1*7 % 9 = 7       (result X base mod c)

# now the result has 7
# SQUARE: 7**2 % 9 = 4         (result x power mod c)
# MULTIPLY: skip, current bit is 0 

# now the result has 4
# SQUARE: 4**2 % 9 = 7         (result x power mod c)
# MULTIPLY: 7*7 % 9 = 4        (result X base mod c)

# 101 (three bits completed) result stores 4 
# ANSWER IS 4
