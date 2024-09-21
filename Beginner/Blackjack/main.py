from art import logo
import random

card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
dealer_cards = []

def deal_cards():
    if len(player_cards) > 0:
        dealer_cards.append(random.choice(card_deck))
        if sum(dealer_cards) > 10:
            possible_hit = random.choice(card_deck)
            if possible_hit == 11:
                dealer_cards.append(1)
        dealer_cards.append(random.choice(card_deck))
    elif len(player_cards) == 0:
        dealer_cards.append(random.choice(card_deck))

    player_cards.append(random.choice(card_deck))
    if sum(player_cards) > 10:
        possible_hit = random.choice(card_deck)
        if possible_hit == 11:
            player_cards.append(1)
    player_cards.append(random.choice(card_deck))
    if sum(player_cards) == 21:
        show_cards()
        print("Win with a Blackjack!!!")
        play()

def hit(person):
    if sum(person) <= 10:
        person.append(random.choice(card_deck))
    elif sum(person) > 10:
        possible_hit = random.choice(card_deck)
        if possible_hit == 11:
            person.append(1)
        else:
            person.append(possible_hit)

def show_cards():
    print(f"    Your cards: {player_cards}, score: {sum(player_cards)}")
    if len(dealer_cards) <= 1:
        print(f"    Dealer's first card: {dealer_cards}")
    else:
        print(f"    Dealer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}")

def ask_hit():
    answer = input("Type 'h' to hit, type 's' to stand: ").lower()
    if answer == "h":
        hit(player_cards)
        show_cards()
        if sum(player_cards) > 21:
            print("You went over. You lose :(")
            play()
        ask_hit()
    elif answer == "s":
        while sum(dealer_cards) < 17:
            hit(dealer_cards)
        show_cards()
        if sum(dealer_cards) > 21:
            print("Opponent went over. You win!!!")
            play()
        elif sum(dealer_cards) > sum(player_cards):
            print("You lose :(")
            play()
        elif sum(player_cards) > sum(dealer_cards):
            print("You win!!!")
            play()
        elif sum(dealer_cards) == sum(player_cards):
            print("You tie and break even :/")
            play()

def play():
    player_cards.clear()
    dealer_cards.clear()
    start_game = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if start_game == "y":
        print("\n" * 20)
        deal_cards()
        print(logo)
        show_cards()
        ask_hit()
    elif start_game == "n":
        return
    else:
        print("Invalid input. Will ask again.")
        play()

play()
