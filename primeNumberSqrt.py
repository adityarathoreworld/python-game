### Simple logic to find prime number for beginners to learn
### Large number will take long time for result due to in-efficient method. will post better method later :)
from math import *
print("Let's see if you got a prime number!!!!")
Number = int(input('enter a number: '))
### finding square root for this number
numsqrt= ceil(sqrt(Number))

### creating list of prime number upto 'numsqrt' for range of multiples
factors = [2,3,5,7,9] ### basic primes from 1 - 10
for num in range(10, numsqrt):
    if num > 1:
        for i in range (2,  num):
            if num % i == 0:
                break
            elif num not in factors:
                factors.append(num)
### checking if your number is prime is simple now lets see
for x in factors:
    if Number % x == 0:
        print(f"{Number} is not a prime number {x} is a factor")
        break
else:
    print(f"{Number} is a prime number")