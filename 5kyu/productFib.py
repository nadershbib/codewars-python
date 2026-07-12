

# https://www.codewars.com/kata/5541f58a944b85ce6d00006a/train/python

# passing solution

def product_fib(_prod):
    fib = [0,1]
    while True:
        if(fib[-2]*fib[-1] >= _prod):
            return [fib[-2],fib[-1],_prod == fib[-2]*fib[-1]]
        fib.append(sum(fib[-2:]))
print(product_fib(10))






