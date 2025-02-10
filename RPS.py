#RPS.py
#Name:
#Date:
#Assignment:
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.
  computer = random.choice( ["R", "P", "S"])
  User_choice = input("Enter R for Rock, P for Paper, or S for Scissors (or Q to Quit): ").upper()
  if user_choice == 'Q': break 
  #Randomly choose the computer between 'R', 'P', or 'S'
  if user_choice is not [ 'R', 'P', 'S']:
    print("Invalid choice")
  #Prompt the user for their RPS selection
  if user_choice == computer_choice: 
    print("It's a tie.")
    ties = ties + 1
    elif (user_choice == 'R' and computer_choice == 'S'); or \
        (user_choice == 'P' and computer_choice == 'R') or \
        (user_choice == 'S' and computer_choice == 'P'): 
  print("you win!! {user_choice} beats {computer_choice}.")
  wins = wins +1
 else: 
print( "You lose! {computer_choice} beats {user_choice}.")
losses = losses + 1 
  #Determine winner and state what happened to the user
  #Ask the user if they would like to play again.

  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
