import random
from os import system

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

class Hand:
  def __init__(self):
    self.hand = []
    self.total = 0

  def draw(self):
    card = cards[random.randint(0, len(cards) - 1)]
    self.hand.append(card)
    self.total += card
    if self.total > 21:
      if 11 in self.hand:
        ace = self.hand.index(11)
        self.hand[ace] = 1

def new_game():
  player_hand = Hand()
  player_hand.draw()
  player_hand.draw()

  dealer_hand = Hand()
  dealer_hand.draw()
  dealer_hand.draw()

  while True:
    system('cls')
    print(logo)
    print(f"Your cards: {player_hand.hand}")
    print(f"Dealer first card: {dealer_hand.hand[0]}")
    if player_hand.total >= 21: 
      if player_hand.total == 21: 
        print("Your hand equals 21, you win!")
      else:
        print(f"Bust! your hand equals {player_hand.total}")
      break

    player_choice = input("Would you like to hit or stay? Type 'h' or 's': ")
    if player_choice == 'h':
      player_hand.draw()
    else:
      while dealer_hand.total < 17:
        dealer_hand.draw()
      system('cls')
      print(logo)
      print(f"Your cards: {player_hand.hand}")
      print(f"Dealer's cards: {dealer_hand.hand}")
      if dealer_hand.total > 21:
        print("Dealer bust! You win!")
        break
      if dealer_hand.total >= player_hand.total:
        print("Dealer has a greater hand. You Lose!")
        break

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

while play == 'y':
  new_game()
  play = input("Would you like to play again? Type 'y' or 'n': ")