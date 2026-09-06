# EXTRACTION OF DIGITS IN REVERSE FASHION
# FOR EXAMPLE: 7789
# EXTRACT DIGITS ONE BY ONE IN A REVERSE FASHION 
# You could use the modulus operator to extract the last digit of the number and then use integer division to remove the last digit from the number. Repeat this process until the number becomes zero.


# PSEUDO CODE
# Take an input n from the user 
# while n > 0
# last digit = n % 10
# print (last digit)
# n = n//10

n = int(input("Enter a number: "))
i = 0
while n > 0:
    
    last_digit = n%10
    print(i)
    n //= 10
# Given a number n, find out and return the number of digits present in a number 

n = "156"
print(len(n))

