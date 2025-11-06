score = 0 
play_again = True
#create a while loop to continue the game
while play_again:
#reset the score of tic tac toe 
    score = 0 
print(f"your score is currently: {score}")
the_players_response = input("would you like to play again? (yes/no): ")
if the_players_response.lower() != 'yes':
    play_again = False 

