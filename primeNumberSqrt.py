### Simple logic to find prime number for beginners to learn
from math import *
print("Let's see if you got a prime number!!!!")
Number = int(input('enter a number: '))
### finding square root for this number
numsqrt= ceil(sqrt(Number))
### identify when to stop query
QueryComplete = False
### assuming number is prime
isPrime = True 
### Iteration Range to get prime
for num in range(2, numsqrt):
###if number is prime 
    if QueryComplete == False: 
        for i in range (2,  num):
            if num % i == 0:
                break
### i is prime in this case hence we can use it to check if our number is prime or not
            elif Number % i == 0: 
                print(f"{Number} is not a prime number {i} is a factor")
                QueryComplete = True
                isPrime = False ### condition failed number is not a prime number
                break
if isPrime == True:
    print(f"{Number} is a prime number")
