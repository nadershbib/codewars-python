import math
def list_squared(m, n):

    finalList = []
    for num in range(m,n+1):
        divisors = []
        for i in range(1,math.isqrt(num)+1):
             if num % i == 0:
                other = num // i
                divisors.append(i ** 2)

                if other != i:
                    divisors.append(other ** 2)
        sumOfSquaredDivisors = sum(divisors)
        if math.isqrt(sumOfSquaredDivisors) ** 2 == sumOfSquaredDivisors:
            finalList.append([num,sumOfSquaredDivisors])
    return finalList

print(list_squared(1,250))

