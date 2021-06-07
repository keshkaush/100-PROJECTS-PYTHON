from replit import clear
from art import  logo
print(logo)
print('Welcome to blind bidding : \n')

bidding_dict = {}
any_bidder = False

def checking_bid(final_dict):
    higest_bid = 0
    higest_bidder = ""
    for bidder in final_dict:
        bid_amount = final_dict[bidder]
        if bid_amount > higest_bid:
            higest_bid = bid_amount
            higest_bidder = bidder
    print(f"{higest_bidder} won the bidding by bidding ${higest_bid}")        

while not any_bidder:
    name = input("Name of the bidder : ")
    price = int(input("Price you want to Bid : $"))
    bidding_dict[name] = price
    any_other_bidder = input("Are there any other bidders :")
    if any_other_bidder == "no":
        any_bidder = True
        checking_bid(bidding_dict)  
    else:
        clear()          # use a function to clear screen.!!
