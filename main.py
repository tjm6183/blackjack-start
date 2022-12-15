import random
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
user_total = 0
computer_total = 0
yes_or_no = 'y'

def calculation():
  user_total = 0
  for card in user_cards:
    user_total = user_total + card
    
  print(f"Your final total is {user_total}.")

  computer_total = 0
  
  for card in computer_cards:
    computer_total = computer_total + card

  while user_total <= 21 and computer_total <= 16:
    additional_computer_card = random.choice(cards)
    computer_cards.append(additional_computer_card)
    computer_total = computer_total + additional_computer_card
    
  print(f"The computer had {computer_cards}. The computer's total is {computer_total}.")

  if user_total > 21:
    print("Bust! Computer wins.") 
  elif computer_total > 21:
    print("The computer busted! You win!")
  elif user_total > computer_total:
    print("You win!")
  elif computer_total > user_total:
    print("You lost!")
  elif user_total == computer_total:
    print("You tied!")
    


while yes_or_no == 'y':
  
  user_total = 0
  computer_total = 0
  user_cards = []
  computer_cards = []
  
  yes_or_no = input("Would you like to play a game of blackjack? Type 'y' or 'n'. ")
  if yes_or_no == 'n':
    exit()
  else:
    clear()
    
  print("""
   _     _            _    _            _    
  | |   | |          | |  (_)          | |   
  | |__ | | __ _  ___| | ___  __ _  ___| | __
  | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
  | |_) | | (_| | (__|   <| | (_| | (__|   < 
  |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\/
                         _/ |                
                        |__/
  """)
  
  user_card_1 = random.choice(cards)
  user_cards.append(user_card_1)
  user_card_2 = random.choice(cards)
  user_cards.append(user_card_2)
  
  
  print(f"Your cards are {user_card_1} and {user_card_2}.")
  
  computer_card_1 = random.choice(cards)
  computer_cards.append(computer_card_1)
  computer_card_2 = random.choice(cards)
  computer_cards.append(computer_card_2)
  
  print(f"The computer's face-up card is {computer_card_1}.")
  
  initial_choice = input("Would you like to hit? Type 'y' or 'n'. ")
  
  while initial_choice == 'y':
    user_total = 0
    additional_user_card = random.choice(cards)
    user_cards.append(additional_user_card)
    
      
    print(f"You receive a(n) {additional_user_card}.")
  
    
    for card in user_cards:
      user_total = user_total + card
  
    if user_cards.count(11) > 0 and user_total > 21:
      ace_location = user_cards.index(11)
      user_cards[ace_location] = 1
      user_total = 0 
      for card in user_cards:
        user_total = user_total + card
      print("Your ace was converted from an 11 to a 1.")
    
    print(f"This makes your new total: {user_total}.")
  
    if user_total > 21:
      break
      
    initial_choice = input("Would you like to hit again? Type 'y' or 'n'. ")

    
  calculation()
  
