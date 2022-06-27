import random
option = ['rock', 'paper' , 'scissor']
playagain = "yes"
def play():
    for x in option:
        print(x)
    print('go')
    print('Choose from rock, paper or scissor')
    Gesture = input("Enter your choice ");
    computer = str(random.choice(option))
    print(computer)
    if Gesture not in option:
        Gesture = input("Enter valid choice between rock, paper or scissor - ")
    if(computer == Gesture):
        print("Its a draw computer selected %s" % computer)
    elif(computer == "rock"):
        if(Gesture == "paper"):
            print("You won, computer had selected %s" % computer)
        else:
            print("you lost, computer had selected %s" % computer)
    elif(computer == "paper"):
        if(Gesture == "scissor"):
            print("You won, computer had selected %s" % computer)
        else:
            print("you lost, computer had selected %s" % computer)
    elif(computer == "scissor"):
        if(Gesture == "rock"):
            print("You won, computer had selected %s" % computer)
        else:
            print("you lost, computer had selected %s" % computer)
while playagain == "yes":
    play()
    playagain = input("wanna play again? Enter yes or no - ")

        
    
