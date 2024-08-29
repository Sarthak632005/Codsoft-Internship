import random

def user_choice():
    choice = input("\nEnter your choice (rock, paper, or scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        choice = input("Invalid choice! Please enter rock, paper, or scissors: ").lower()
    return choice

def computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "\nIt's a TIE round", 0
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "\nYou won the round !", 1
    else:
        return "\nComputer won the round!", -1
        
def play_game():
    while True:
        def user_choice():
            choice = input("\nEnter your choice (rock, paper, or scissors): ").lower()
            while choice not in ['rock', 'paper', 'scissor']:
                choice = input("Invalid choice! Please enter rock, paper, or scissors: ").lower()
            return choice

        def computer_choice():
            return random.choice(["rock", "paper", "scissor"])

        def determine_winner(user, computer):
            if user == computer:
                return "\nIt's a TIE round", 0
            elif (user == "rock" and computer == "scissor") or \
                 (user == "paper" and computer == "rock") or \
                 (user == "scissor" and computer == "paper"):
                return "\nYou won the round !", 1
            else:
                return "\nComputer won the round!", -1
        
        total_rounds = int(input("How many rounds do you want to play? "))
        user_score = 0
        computer_score = 0
        round_stats = []

        for round_number in range(1, total_rounds + 1):
            print(f"\nRound {round_number}:")
            user = user_choice()
            computer = computer_choice()

            print(f"\nUser's Choice: {user}")
            print(f"Computer's Choice: {computer}")

            result, score = determine_winner(user, computer)
            print(result)
            
            if score == 1:
                user_score += 1
            elif score == -1:
                computer_score += 1

            round_stats.append((round_number, user, computer))

            print(f"Score -> You: {user_score} | Computer: {computer_score}")
        
        print("\n--- END OF ROUNDS ---\nFinal Score:")
        print(f"You: {user_score} | Computer: {computer_score}")
        
        if user_score > computer_score:
            print("Congratulations, you won the game!")
        elif user_score < computer_score:
            print("Computer wins the game! Better luck next time.")
        else:
            print("The game is a tie!")
            
        print("\nRound-by-Round Stats:")
        
        for stat in round_stats:
            round_num, user_choice, computer_choice = stat
            
            print(f"Round {round_num}: You chose {user_choice}, Computer chose {computer_choice}")

        play_again = input("\nDo you want to play again (yes/no): ").lower()
        if play_again != "yes":
            break

        
play_game()
