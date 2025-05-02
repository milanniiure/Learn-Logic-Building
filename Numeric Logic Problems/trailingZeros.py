# how does this work?
# A trailing zero is formed by multiplication of 5 and 2. so if we consider all prime factors of all numbers from 1 to n
# there would be more 2s than 5s. so the number of 0s is limited by number of 5s. If we count the number of 5s in prime
# factors, we get the result. 
# Example: 
# n=5 and 5! (5*4*3*2*1) has one 5 and three 2s (5*2*2*3*2*1). So the count of trailing 0s is min(1,3) = 1
# n=11 and 11! (11*10*9*8*7*6*5*4*3*2*1) has (11*5*2*3*3*2*2*2*7*2*3*5*2*2*3*2*1) has two 5s and eight 2s. 
# so the count of trailing 0 is min(8, 2) = 2
