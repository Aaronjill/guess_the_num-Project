import random
from art import logo

def random_num():
  num=random.randint(1,100)
  return(num)
num=random_num()

def compare(user_num,num):
  if user_num>num:
    print("TOO HIGH\nGuess Again")
    return 1
  elif user_num<num:
    print("TOO LOW\nGuess Again")
    return 1
  elif user_num==num:
    print("You guessed it right, The number was:",num)
    return 0

def play_game():
  print(logo)
  
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
        
  mode=input("Choose a difficulty. Type 'easy' or 'hard'")
  if mode == 'easy':
    turn=10
  else:
    turn=5
  con=False
  while con == False:
    user_num=int(input("Make a guess: "))
    ans=compare(user_num,num)    
    if ans==1:
      turn-=1
      print("\nYou have",turn,"attempts remaining to guess the number.")
    else:
      con=True
    if turn == 0:
      con=True
      print("You dont have any lives left",turn,"\nThe num was:",num)
play_game()