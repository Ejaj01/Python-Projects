import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]
options[0] = "rock"
options[1] = "paper"
options[2] = "scissors"


while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        print("Maybe another time!")
        break
    
    if user_input not in options:
        print("Please type Rock, Paper, Scissors or Q to quit.")
        continue

    random_number = random.randint(0, 2)
    #rock is 0, paper is 1, scissors is 2
    computer_pick = options[random_number]
    print("Computer picked " + str(computer_pick) + ".")


    if user_input == "rock" and computer_pick == "scissors":
        print("You win!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You win!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You win!")
        user_wins += 1

    elif user_input == computer_pick:
        print("It's a tie!")

    else:
        print("You lose!")
        computer_wins += 1


print("You won " + str(user_wins) + " times.")
print("The computer won " + str(computer_wins) + " times.")

if user_wins == computer_wins:
    print("It's a tie overall!")
print("Goodbye!")
