import random
count=0
def get_my_choice():
    my_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    while my_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please select again.")
        my_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    return my_choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(my_choice, computer_choice):
    if my_choice == computer_choice:
        return "It's a tie!"
    elif (
        (my_choice == 'rock' and computer_choice == 'scissors') or
        (my_choice == 'paper' and computer_choice == 'rock') or
        (my_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "Hurray! You won the Game!"
    else:
        return "Oops! Better luck next time."

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    while True:
        my_choice = get_my_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {my_choice}")
        print(f"Computer chose: {computer_choice}")
        print(determine_winner(my_choice, computer_choice))
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    play_game()
