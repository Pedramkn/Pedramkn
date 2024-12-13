import random
import sys

# Define global scores
user_score = 0
computer_score = 0

# Define possible choices
choices = ['rock', 'paper', 'scissors']

# Define comments
win_comments = [
    "Great job!", "Nice move!", "Well played!", "You nailed it!",
    "Keep it up!", "You're unstoppable!", "You're on fire!", "Awesome!",
    "Good one!", "Smart move!"
]
lose_comments = [
    "Too bad!", "Try again!", "Not your round!", "Close call!",
    "You'll get it!", "Keep going!", "Stay strong!", "Almost!",
    "Better luck!", "Oops!"
]
tie_comments = [
    "It's a draw!", "So close!", "Even match!", "Try again!",
    "Stalemate!", "Deadlock!", "Neck and neck!", "What a tie!",
    "No winner!", "Equal game!"
]

# Determine the winner and generate the result message
def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    if user_choice == computer_choice:
        comment = random.choice(tie_comments)
        return f"It's a tie! {comment}"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        user_score += 1
        comment = random.choice(win_comments)
        return f"You win! {comment}"
    else:
        computer_score += 1
        comment = random.choice(lose_comments)
        return f"Computer wins! {comment}"

# Main game loop
def main():
    global user_score, computer_score
    print("Welcome to Rock, Paper, Scissors!")

    round_count = 0
    while True:
        try:
            print("\nChoose your option:")
            print("1. Rock")
            print("2. Paper")
            print("3. Scissors")
            print("4. Quit")
            
            user_input = input("Enter your choice (1/2/3/4): ").strip()
            
            # Quit condition
            if user_input == '4':
                print("\nFinal Scores:")
                print(f"You: {user_score}, Computer: {computer_score}")
                print("Thanks for playing!")
                break

            # Handle invalid input
            if user_input not in ['1', '2', '3']:
                print("Invalid input, please try again.")
                continue

            # Process user and computer choices
            user_choice = choices[int(user_input) - 1]
            computer_choice = random.choice(choices)
            
            print(f"\nYou chose: {user_choice}")
            print(f"Computer chose: {computer_choice}")
            
            # Determine and display the result
            result = determine_winner(user_choice, computer_choice)
            print(result)

            round_count += 1

            # After every 5 rounds, ask if the user wants to continue
            if round_count % 5 == 0:
                print("\n--- 5 Games Completed ---")
                print(f"Scores so far -> You: {user_score}, Computer: {computer_score}")
                continue_game = input("Do you want to continue? (yes/no): ").strip().lower()
                if continue_game != 'yes':
                    print("\nFinal Scores:")
                    print(f"You: {user_score}, Computer: {computer_score}")
                    print("Thanks for playing!")
                    break

        except KeyboardInterrupt:
            print("\n\nGame interrupted. Exiting gracefully...")
            print(f"Final Scores -> You: {user_score}, Computer: {computer_score}")
            print("Thanks for playing!")
            sys.exit()

# Start the game
if __name__ == "__main__":
    main()
