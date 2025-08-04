import random
print("now running rockpaperscissor")
options = ["rock", "paper", "scissor"]
while True:
    player_move = input("Rock, Paper, or Scissor?\n").lower()
    if player_move not in options:
        print("Try again.")
        continue
    computer_move = random.choice(options)
    print(f"You chose {player_move}.")
    print(f"Computer chose {computer_move}.")
    if player_move == computer_move:
        print("Tie")
    elif (
        (player_move == "rock" and computer_move == "scissor") or
        (player_move == "scissor" and computer_move == "paper") or
        (player_move == "paper" and computer_move == "rock")
    ) :
      print("You win")
    else:
        print("Computer wins")
    play_again = input("Play again? (y/n)").lower()
    if play_again != "y":
        print("bye")
        break
    else:
        continue            

