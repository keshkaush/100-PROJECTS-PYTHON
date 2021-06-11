from art import logo
import random
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def get_card():
    random_card = random.choice(cards)
    return random_card

user_list = []
comp_list = []

user_list.extend([get_card(), get_card()])
comp_list.extend([get_card(), get_card()])

will_continue = True

def calculate_score(player_list, dealer_list):
    dealer_list_score = sum(comp_list)
    player_list_score = sum(user_list)

    if dealer_list_score < 17:
        comp_list.append(get_card())
        dealer_list_score = sum(comp_list)
    if (dealer_list[0] == 10 and dealer_list[1] == 11) or (dealer_list[1] == 10 and dealer_list[0] == 11):
        return 0
    elif (player_list[0] == 10 and player_list[1] == 11) or (player_list[1] == 10 and player_list[0] == 11):
        return 2    
    if dealer_list_score > player_list_score:
        return -1
    elif dealer_list_score < player_list_score:
        return 1    

while will_continue:
    print(logo)
    will_play = input("DO YOU WANT TO PLAY BlackJack ? type 'y' or 'n' as an response !! : ")
    if will_play == "y":
        print(f"Your cards are : {user_list}, and your current score is : {sum(user_list)}")
        print(f"Dealers 1st card is : {comp_list[0]} ")
        if calculate_score(user_list, comp_list) == 0:
            print(f"Player cards are these : {user_list} \nDealer got a BlackJack with these cards : {comp_list} \nSo you Loose..!!!")
        elif calculate_score(user_list, comp_list) == 2:
            print(f"Dealer cards are these : {comp_list} \nYou got a BlackJack with these cards : {user_list} \nSo you Win..!!!")    
        else:
            want_hit = input("Do you want to take a hit? reply in 'y' or 'n' !!") 
            player_list_score = sum(user_list)
            if want_hit == "y":
                user_list.append(get_card())
                player_list_score = sum(user_list)
            if player_list_score > 21:
                print(f"Player cards are these : {user_list} \nYour Final Score : {player_list_score} \nSo you Loose..!!!")
            else:
                if calculate_score(user_list, comp_list) == 1:
                    print(f"Player cards are these : {user_list} with Score : {sum(user_list)} \nDealer have these cards : {comp_list} with Score : {sum(comp_list)}\nSo you Win..!!!")    
                elif calculate_score(user_list, comp_list) == -1:
                    print(f"Player cards are these : {user_list} with Score : {sum(user_list)}\nDealer have these cards : {comp_list} with Score : {sum(comp_list)}\nSo you Loose..!!!")            
    new_game = input("Another round ? type 'y' or 'n' !! : ")
    if new_game == "y":
        clear()
    else: 
        will_continue = False
        print("Thank You shoing your interest !!")
