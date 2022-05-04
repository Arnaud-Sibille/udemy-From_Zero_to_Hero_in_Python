from deck import Deck
from player import Player

def ft_add_player(players):
    while True:
        bol = True
        name = input("Please enter player name: ")
        for item in players:
            if (item.name == name):
                print("Already existing name.")
                bol = False
        if bol:
            break
    while True:
        try:
            money = int(input("Please enter the amount of money: "))
            break
        except:
            print("Please enter a valid amount.")
    play = Player(name, money)
    players.append(play)

def ft_rem_player(players):
    name = input("Please enter player name: ")
    for item in players:
        if (item.name == name):
            if (item.money >= 0):
                print(f"The casino owes {name} {item.money}$.")
            else:
                print(f"{name} owes the casino {item.money}$.")
            print(f"{name} left the game.")
            return 0
    print(f"Failed to remove {name}.")

def ft_play_a_game(players):
    print("Hello everyone, who's up for a Blackjack game?")
    del_player = True
    while del_player:
        print(f"Currently there are {len(players)} players: ")
        for item in players:
            print(f"{item.name} : {item.money}$")
        while True:
            ans = input("Does a player wants to stop playing? (yes/no): ")
            if ans == "yes":
                ft_rem_player(players)
                break
            if ans == "no":
                del_player = False
                break
            print("Please enter a valid answer. ")
    new_player = True
    while new_player:
        print(f"Currently there are {len(players)} players: ")
        for item in players:
            print(f"{item.name} : {item.money}$")
        if len(players) >= 5:
            print("The max number of player is reached, no more player can be added.")
            new_player = False
            break
        while True:
            ans = input("Do you want to add a new player? (yes/no): ")
            if ans == "yes":
                ft_add_player(players)
                break
            if ans == "no":
                new_player = False
                break
            print("Please enter a valid answer. ")
    if len(players) > 0:
        print("Okay, let's start the game! ")
        return 1
    print("No more players, thank you for playing! ")
    return 0
