# https://www.codewars.com/kata/56b7251b81290caf76000978/train/python

def get_last_digit(index):
   a,b = 0,1 
   for i in range(index - 1):
      a,b = b,(a+b)%10
   return b

# (a+b) % 10 == ((a % 10) + (b % 10)) % 10

# that's why for this problem there is no need to actually calculate each Fibonacci then manually extracting last digit
# with mod arithmetic law, by simply storing last digit of every fib, it would get you last digit of the fib you'd want


    