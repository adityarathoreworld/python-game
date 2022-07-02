### Simple logic to find prime number for beginners to learn
### Large number will take long time for result due to in-efficient method. will post better method later :)
from math import *
print("Let's see if you got a prime number!!!!")
Number = int(input('enter a number: '))
### finding square root for this number
numsqrt= ceil(sqrt(Number))

### creating list of prime number upto 'numsqrt' for range of multiples
QueryComplete = False ### identify when to stop query
isPrime = True ### assuming number is prime
for num in range(2, numsqrt): ### Iteration Range to get prime
    if QueryComplete == False: ###if number is prime 
        for i in range (2,  num):
            if num % i == 0:
                break
            elif Number % i == 0:
                print(f"{Number} is not a prime number {i} is a factor")
                QueryComplete = True
                isPrime = False ### condition failed number is not a prime number
                break
    
if isPrime == True:
    print(f"{Number} is a prime number")
