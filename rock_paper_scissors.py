def RPC():
    while True:
        player1 = input("Player 1: Select: \n Rock \n Paper \n Scissors \n  ").strip().lower()
        player2 = input("Player 2: Select: \n Rock \n Paper \n Scissors \n  ").strip().lower()
        
        valid_choices = {"rock", "paper", "scissors"}
        if player1 not in valid_choices or player2 not in valid_choices:
            print("Invalid input! Please enter rock, paper, or scissors.")
            continue

        if (player1 == "rock" and player2 == "scissors" or
            player1 == "paper" and player2 == "rock" or
            player1 == "scissors" and player2 == "paper"):
            print("Player 1: Won")
        elif (player1 == "rock" and player2 == "paper" or
              player1 == "paper" and player2 == "scissors" or
              player1 == "scissors" and player2 == "rock"):
            print("Player 2: Won")
        else:
            print("Match draw")
        
        playagain = input("Do you want to play again? (yes/no): ").strip().lower()
        if playagain == "no":
            break

RPC()
