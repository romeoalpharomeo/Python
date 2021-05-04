"""
Build and application when both a user and computer can select either Rock, Paper or Scissors, determine the winner, and display the results

For reference:

Rock beats Scissors
Scissors beats Paper
Paper beats Rock
Part I
Compare user input agains computer choice and determine a winner

Part II
Compare user input agains computer choice and determine a winner.  The winner will be the best 5 games, and end as soon at someone wins 3 games.
"""

player_win_count = 0
computer_win_count = 0
while player_win_count < 3 or computer_win_count < 3:
    import random
    computer_options = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(computer_options)
    player_choice = input('Rock, paper, scissors, shoot!: ')
    if player_choice == computer_choice:
        print("TIE!")
    elif player_choice == "Rock":
        if computer_choice == "Scissors":
            print("Player wins!")
            player_win_count += 1

        else:
            print("Player loses.")
            computer_win_count += 1
                
    elif player_choice == "Paper":
        if computer_choice == "Rock":
            print("Player wins!")
            player_win_count += 1
                
        else:
            print("Player loses.")
            computer_win_count += 1
                
    elif player_choice == "Scissors":
        if computer_choice == "Paper":
            print("Player wins!")
            player_win_count += 1
                
        else:
            print("Player loses.")
            computer_win_count += 1

if player_win_count > computer_win_count:
    print('Player won the game!')
else:
    print('Computer won the game.')