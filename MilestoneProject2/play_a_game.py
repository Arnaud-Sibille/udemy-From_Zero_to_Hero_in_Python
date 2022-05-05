from deck import Deck
from player import Player
from print_players import ft_print_players
from utils import get_ans1
from utils import get_ans2
from utils import get_ans3
from utils import get_ans4

def ft_add_player(players):
    play = Player(get_ans3(players), get_ans4())
    players.append(play)

def ft_rem_player(players):
    name = input("Please enter player name: ")
    for item in players:
        if (item.name == name):
            print(f"The casino owes {name} {item.money}$.")
            players.remove(item)
            print(f"{name} left the game.")
            return 0
    print(f"Failed to remove {name}.")

def remove_broke_players(players):
    rem = []
    for play in players:
        if play.money < 2:
            rem.append(play)
    for play in rem:
        players.remove(play)
        print(f"{play.name} has been kicked out because he has not enough money.  The casino owes him {play.money}$.")

def ft_del_players(players):
    if len(players) > 0:
        del_player = True
        while del_player:
            print(f"Currently there are {len(players)} players: ")
            ft_print_players(players, None, 0)
            ans = get_ans1()
            if ans == "yes":
                ft_rem_player(players)
            elif ans == "no":
                del_player = False
            if len(players) == 0:
                del_player = False

def ft_add_players(players):
    new_player = True
    while new_player:
        print(f"Currently there are {len(players)} players: ")
        ft_print_players(players, None, 0)
        if len(players) >= 5:
            print("The max number of player is reached, no more player can be added.")
            new_player = False
            break
        ans = get_ans2()
        if ans == "yes":
            ft_add_player(players)
        if ans == "no":
            new_player = False

def ft_play_a_game(players):
    remove_broke_players(players)
    print("Hello everyone, who's up for a Blackjack game?")
    ft_del_players(players)
    ft_add_players(players)
    if len(players) > 0:
        print("Okay, let's start the game! ")
        return 1
    print("No more players, thank you for playing! ")
    return 0
