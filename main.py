#display art
from art import logo, vs
import random
from game_data import data
from replit import clear

score = 0
account_b = random.choice(data)
print(logo)
#make the game repeatable
not_game_over = True
while not_game_over:
#format the data into printable format
  def format(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_description}, from {account_country}"

  #check is user guess is correct
  ##get follower count of each account
  def check_answers(guess,a_followers,b_followers):
    if a_followers > b_followers:
      return user_guess=='a'
    else:
      return user_guess=='b'

  #generate random number
  account_a = account_b
  account_b = random.choice(data)
  while account_a == account_b:
    account_b = random.choice(data)
  
  print(f"Compare A: {format(account_a)}")
  print(vs)
  print(f"Against B: {format(account_b)}")

  #ask user for a guess
  user_guess = input("Who has more followers? Type 'A' or 'B':").lower()

  #check is user guess is correct
  ##get follower count of each account
  ##use if statement to check if user is correct
  a_follower_count = account_a['follower_count']
  b_follower_count = account_b['follower_count']
  is_correct = check_answers(user_guess,a_follower_count,b_follower_count)
  
  clear()
  print(logo)
  #give user feedback on their guesses
  #score keeping
  if is_correct:
    score += 1
    print(f"You are right! Current score: {score}")
  else:
    not_game_over = False
    print(f"You are wrong! Current score: {score}")
 
#make account at position B become the next account at position A 

#clear the screen between rounds

































# from art import logo, vs
# import random
# from game_data import data
# from replit import clear

# game_over = False
# score = 0
# while not game_over:
#   print(logo)
#   l = []
#   random_num = random.randint(0,3)
#   l.append(random_num)
#   celebA_info = data[random_num]
#   print(f"Compare A: {celebA_info['name']},{celebA_info['description']}, from {celebA_info['country']}")

#   print(vs)

#   random_num = random.randint(0,3)
#   while random_num not in l:
#     celebB_info = data[random_num]
#     print(f"Against B:{celebB_info['name']},{celebB_info['description']}, from {celebB_info['country']}")
#     break
#   else:
#     random_num = random.randint(0,3)
#     celebB_info = data[random_num]
#     print(f"Against B:{celebB_info['name']},{celebB_info['description']}, from {celebB_info['country']}")

#   user_guess = input("Who has more followers? Type 'A' or 'B':")
#   print(user_guess)
#   if user_guess == 'A':
#     if celebA_info['follower_count'] > celebB_info['follower_count']:
#       clear()
#       score += 1
#       print(f"You are right! Current score: {score}")    
#     else:
#       clear()
#       print(f"You are wrong! Final score:{score}")
#       break    
#   elif user_guess == 'B':
#     if celebA_info['follower_count'] < celebB_info['follower_count']:
#       clear()
#       score += 1
#       print(f"You are right! Current score: {score}") 
#     else:
#       clear()
#       print(f"You are wrong! Final score:{score}")
#       break    
#   else:
#     clear()
#     print(f"You are wrong! Final score:{score}")
#     break

  
    
  


  
