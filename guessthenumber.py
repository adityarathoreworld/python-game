import random
print("Welcome to number guess game!!!")
### setting range for game play!!
start = 1 
end = 99 
### generating random number between 1 and 99
computer = random.randint(start, end)
userGuess = int(input(f"Guess the number between {start} and {end} "))
### helping user with hints
while userGuess != computer:
    if(userGuess > computer):
        print(f"hidden number is lower than {userGuess}")
        userGuess = int(input("Guess the number? "))
    else:
        print(f"hidden number is higher than {userGuess}")
        userGuess = int(input("Guess the number? "))
print("Congratulations you win!!")

