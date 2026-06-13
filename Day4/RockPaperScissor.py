import random

choices = ["Rock", "Paper", "Scissors"]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))

if user_choice < 0 or user_choice > 2:
    print("Invalid choice!")
else:
    print(f"\nYou chose: {choices[user_choice]}")

    computer_choice = random.randint(0, 2)
    print(f"Computer chose: {choices[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a Draw!")

    elif user_choice == 0 and computer_choice == 2:
        print("You Win!")

    elif user_choice == 2 and computer_choice == 1:
        print("You Win!")

    elif user_choice == 1 and computer_choice == 0:
        print("You Win!")

    else:
        print("You Lose!")
        