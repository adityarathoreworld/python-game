### Simple logic to find prime number for beginners to learn
### Large number will take long time for result due to in-efficient method. will post better method later :)
print("Let's see if you got a prime number!!!!")
Number = int(input('enter a number: '))
for x in range(2,Number-1):
    if Number % x == 0:
        print("Not a prime number it has a factor - %d" % x)
        break
else:
    print("%d is a prime number" % Number)
