# Fizz Buzz #2
# Write a function to print all numbers 1 to n, but there are some constraints
# If the number is divisible by 3, print ‘Fizz’ instead of the number
# If the number is divisible 5, print ‘Buzz’ instead of the number
# If the number is divisible by both 3 and 5, print ‘FizzBuzz’ instead of the number
# Otherwise, simply print the number
# Example Input: 15
# Output:
# 1
# 2
# 'Fizz'
# 4
# 'Buzz'
# 'Fizz'
# 7
# 8
# 'Fizz'
# 'Buzz'
# 11
# 'Fizz'
# 13
# 14
# 'FizzBuzz'

for num in range (1,16):
    if num % 3 == 0 and num % 5 ==0:
        print ('FIZZBUZZ')
    elif num % 3 == 0:
        print ("FIZZ")
    elif num % 5 == 0:
        print ('BUZZ')
    else:
        print (num)